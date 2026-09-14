"""Declared standalone package inputs and dependency closure."""
from source_resources import check_resource_closure
from secure_io import read_bytes


def package_inputs(root, identity, policy):
    base = root / identity
    inputs = {p.relative_to(base).as_posix(): p for p in base.rglob("*") if p.is_file()
              and "__pycache__" not in p.parts}
    copies = dict(policy["copies"].get(identity, {}))
    if identity in policy["covered_skills"]:
        copies.update({p: p for p in policy["shared_files"]})
    for dest, source in copies.items():
        if dest in inputs:
            raise ValueError(f"generated copy collision: {identity}/{dest}")
        inputs[dest] = root / source
    for source in inputs.values():
        read_bytes(source)  # bind every input, including binary/copied resources
    check_resource_closure(inputs)
    return inputs
