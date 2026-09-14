"""Bounded Linux file IO; regular inputs must have exactly one link."""
from contextlib import contextmanager
import os
from pathlib import Path
import stat
import hashlib
from contextvars import ContextVar
from functools import wraps

_seen = ContextVar("secure_io_seen", default=None)


def stable_io(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        if _seen.get() is not None:
            return function(*args, **kwargs)
        token = _seen.set({})
        try:
            return function(*args, **kwargs)
        finally:
            _seen.reset(token)
    return wrapped


def remember(path, value):
    seen = _seen.get()
    if seen is not None:
        key = str(Path(path).absolute())
        if key in seen and seen[key] != value:
            raise ValueError("identity/content changed across operation: " + key)
        seen[key] = value

DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
FILE_FLAGS = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC


@contextmanager
def parent_fd(path):
    path = Path(path).absolute()
    if '..' in path.parts:
        raise ValueError('path traversal forbidden')
    descriptors = [os.open(path.anchor, DIR_FLAGS)]
    chain = []
    current_path = Path(path.anchor)
    try:
        for part in path.parts[1:-1]:
            parent = descriptors[-1]
            before = os.stat(part, dir_fd=parent, follow_symlinks=False)
            fd = os.open(part, DIR_FLAGS, dir_fd=parent)
            descriptors.append(fd)
            if identity(before) != identity(os.fstat(fd)):
                raise ValueError('ancestor identity changed during open')
            chain.append((parent, part, fd))
            current_path /= part
            remember(current_path, identity(os.fstat(fd)))
        check_chain(chain)
        yield descriptors[-1], path.name
        check_chain(chain)
    finally:
        for fd in reversed(descriptors):
            os.close(fd)


def identity(info):
    return info.st_dev, info.st_ino, stat.S_IFMT(info.st_mode)


def check_chain(chain):
    for parent, name, fd in chain:
        if identity(os.stat(name, dir_fd=parent, follow_symlinks=False)) != identity(os.fstat(fd)):
            raise ValueError('ancestor identity changed')


def fingerprint(info):
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink,
            info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def read_optional(path):
    return read_bytes(path, missing_ok=True)


def read_bytes(path, *, missing_ok=False):
    with parent_fd(path) as (parent, name):
        try:
            before = os.stat(name, dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            if not missing_ok:
                raise
            remember(path, None)
            return None
        fd = os.open(name, FILE_FLAGS, dir_fd=parent)
        try:
            info = os.fstat(fd)
            if (before.st_dev, before.st_ino) != (info.st_dev, info.st_ino):
                raise ValueError('file identity changed during open')
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                raise ValueError('single-link regular file required; hardlinks forbidden')
            with os.fdopen(fd, 'rb', closefd=False) as stream:
                content = stream.read()
                stream.seek(0)
                if stream.read() != content:
                    raise ValueError('file content changed during read')
            for current in (os.fstat(fd), os.stat(name, dir_fd=parent, follow_symlinks=False)):
                if fingerprint(current) != fingerprint(before):
                    raise ValueError('file identity/content changed during read')
            remember(path, (fingerprint(before), hashlib.sha256(content).digest()))
            return content
        finally:
            os.close(fd)


def makedirs(path):
    path = Path(path).absolute()
    try:
        with parent_fd(path / '__directory_probe__'):
            return
    except FileNotFoundError:
        makedirs(path.parent)
        mkdir(path, exist_ok=True)


def mkdir(path, mode=0o700, exist_ok=False):
    with parent_fd(path) as (parent, name):
        try:
            os.mkdir(name, mode=mode, dir_fd=parent)
        except FileExistsError:
            if not exist_ok:
                raise
        before = os.stat(name, dir_fd=parent, follow_symlinks=False)
        fd = os.open(name, DIR_FLAGS, dir_fd=parent)
        try:
            if identity(before) != identity(os.fstat(fd)):
                raise ValueError('created directory identity changed')
            remember(path, identity(os.fstat(fd)))
            os.fsync(parent)
        finally:
            os.close(fd)


def write_bytes(path, content, mode=0o600):
    """Exclusive descriptor-relative creation; never truncates an existing file."""
    with parent_fd(path) as (parent, name):
        fd = os.open(name, os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW |
                     os.O_CLOEXEC, 0o600, dir_fd=parent)
        try:
            initial = os.fstat(fd)
            with os.fdopen(fd, 'wb', closefd=False) as stream:
                stream.write(content)
                stream.flush()
            os.fchmod(fd, mode)
            os.fsync(fd)
            current = os.fstat(fd)
            if identity(current) != identity(initial) or current.st_nlink != 1:
                raise ValueError('output identity changed')
            if os.pread(fd, len(content) + 1, 0) != content:
                raise ValueError('output content changed')
            if fingerprint(os.stat(name, dir_fd=parent, follow_symlinks=False)) != fingerprint(current):
                raise ValueError('output identity/content changed')
            remember(path, (fingerprint(current), hashlib.sha256(content).digest()))
            os.fsync(parent)
        finally:
            os.close(fd)


def read_text(path, encoding='utf-8'):
    return read_bytes(path).decode(encoding)
