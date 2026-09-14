"""Build standalone previews/releases; never expand source templates."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import zipfile
import tempfile
import uuid
from secure_io import read_bytes, read_text, write_bytes, stable_io, makedirs
from io import BytesIO
from source_resources import safe_path
from package_layout import package_inputs
from toolkit_validation import validate


# Re-export for callers/tests; one canonical package layout implementation.

@stable_io
def generate(root, output, mode, checked):
    report = {"mode": mode, "release": mode == "release", "packages": {}}
    for identity, name in checked["packages"].items():
        target = output / "skills" / name
        hashes = {}
        for relative, source in package_inputs(root, identity, checked["policy"]).items():
            content = read_bytes(source)
            dest = target / relative
            makedirs(dest.parent)
            write_bytes(dest, content)
            hashes[relative] = hashlib.sha256(content).hexdigest()
        report["packages"][name] = hashes
        manifest = {"source": identity, "companions": checked["policy"]["companions"][identity],
                    "files": hashes, "coverage": identity in checked["policy"]["covered_skills"], "logo_policy": checked["policy"]["logo"]}
        content = (json.dumps(manifest, sort_keys=True) + "\n").encode()
        write_bytes(target / "package-manifest.json", content)
        hashes["package-manifest.json"] = hashlib.sha256(content).hexdigest()
        if mode == "release":
            makedirs(output / "zips")
            buffer = BytesIO()
            with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
                for path in sorted(target.rglob("*")):
                    if path.is_file():
                        archive.writestr(path.relative_to(target).as_posix(), read_bytes(path))
            write_bytes(output / "zips" / f"{name}.zip", buffer.getvalue())
    write_bytes(output / "build-report.json", (json.dumps(report, indent=2) + "\n").encode())
    return report


def verify_packages(root, output, checked, mode):
    """Compare normalized contents against live inputs, not zip timestamps."""
    expected_names = set(checked["packages"].values())
    if {p.name for p in (output / "skills").iterdir()} != expected_names:
        raise ValueError("package inventory mismatch")
    report = json.loads(read_text(output / "build-report.json"))
    if set(report["packages"]) != expected_names or report["release"] != (mode == "release"):
        raise ValueError("report mismatch")
    for identity, name in checked["packages"].items():
        folder = output / "skills" / name
        expected = {rel: read_bytes(path) for rel, path in package_inputs(root, identity, checked["policy"]).items()}
        hashes = {rel: hashlib.sha256(data).hexdigest() for rel, data in expected.items()}
        manifest = {"source": identity, "companions": checked["policy"]["companions"][identity],
                    "files": hashes, "coverage": identity in checked["policy"]["covered_skills"], "logo_policy": checked["policy"]["logo"]}
        expected["package-manifest.json"] = (json.dumps(manifest, sort_keys=True) + "\n").encode()
        actual = {}
        for path in folder.rglob("*"):
            safe_path(folder, path.relative_to(folder).as_posix())
            if path.is_file():
                actual[path.relative_to(folder).as_posix()] = read_bytes(path)
        if actual != expected:
            raise ValueError(f"source/package parity mismatch: {name}")
        if report["packages"][name] != {k: hashlib.sha256(v).hexdigest() for k, v in expected.items()}:
            raise ValueError("report hash mismatch")
        if mode == "release":
            try:
                with zipfile.ZipFile(BytesIO(read_bytes(output / "zips" / f"{name}.zip"))) as archive:
                    names = archive.namelist()
                    if len(names) != len(set(names)) or set(names) != set(expected):
                        raise ValueError("archive paths/inventory mismatch")
                    for info in archive.infolist():
                        safe_path(folder, info.filename)
                        if (info.external_attr >> 16) & 0o170000 == 0o120000:
                            raise ValueError("archive symlink")
                    if archive.testzip() is not None or any(archive.read(k) != v for k, v in expected.items()):
                        raise ValueError("archive CRC/content mismatch")
            except zipfile.BadZipFile as exc:
                raise ValueError("corrupt archive") from exc
    zips = {p.name for p in (output / "zips").glob("*")}
    if zips != ({f"{n}.zip" for n in expected_names} if mode == "release" else set()):
        raise ValueError("archive count mismatch")


def safe_output(root, output):
    output = Path(output).absolute()
    if ".." in output.parts:
        raise ValueError("unsafe output traversal")
    safe_path(Path(output.anchor), output.relative_to(output.anchor).as_posix())
    if (output in {root, Path.home(), Path(output.anchor)} or root.is_relative_to(output)
            or output.is_relative_to(root) and output != root / "dist"):
        raise ValueError("unsafe output directory")
    if output.exists():
        owned = output / ".toolkit-build.json"
        if owned.exists():
            if json.loads(read_text(owned)) != {"owner": "contractor-toolkit", "version": 1}:
                raise ValueError("unknown output owner")
            allowed = {"skills", "zips", "build-report.json", ".toolkit-build.json", "README.md"}
        else:
            allowed = {"README.md"} if output == root / "dist" else set()
        if not output.is_dir() or {p.name for p in output.iterdir()} - allowed:
            raise ValueError("refusing unowned output contents")
        for p in output.rglob("*"):
            safe_path(output, p.relative_to(output).as_posix())
    return output


def promote(stage, output):
    backup = output.with_name(output.name + ".previous-" + uuid.uuid4().hex)
    existed = output.exists()
    if existed:
        output.rename(backup)
    try:
        stage.rename(output)
    except BaseException:
        if existed and not output.exists():
            backup.rename(output)
        raise
    # Keep prior release as a recoverable sibling; never silently delete it.


@stable_io
def build(root, output, mode):
    root = Path(root).absolute()
    checked = validate(root, mode)
    output = safe_output(root, output)
    makedirs(output.parent)
    stage = Path(tempfile.mkdtemp(prefix=f".{output.name}.staging-", dir=output.parent))
    try:
        if (output / "README.md").is_file():
            write_bytes(stage / "README.md", read_bytes(output / "README.md"))
        report = generate(root, stage, mode, checked)
        verify_packages(root, stage, checked, mode)
        # Revalidate source metadata/resources after generation, before promotion.
        if validate(root, mode) != checked:
            raise ValueError("source changed during build")
        write_bytes(stage / ".toolkit-build.json", json.dumps({"owner": "contractor-toolkit", "version": 1}).encode())
        safe_output(root, output)
        promote(stage, output)
        return report
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["release", "template-preview"], default="release")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        result = build(root, args.output_dir or root / "dist", args.mode)
        print(json.dumps({"mode": args.mode, "packages": len(result["packages"])}))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"needs_human: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
