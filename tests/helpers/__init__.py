from __future__ import print_function, division, absolute_import

from contextlib import contextmanager
import os
import difflib
import pytest

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(str(dirpath))
        yield
    finally:
        os.chdir(old_path)


def cast_path(anypath):
    """Cast a py.path.local or a str or a pathlib.Path to a pathlib.Path
    """
    return Path(str(anypath))


def assertMultiLineEqual(first, second, msg=None):
    """Assert that two multi-line strings are equal.
    If they aren't, show a nice diff.
    """
    __tracebackhide__ = True

    if first != second:
        message = ''.join(difflib.ndiff(first.splitlines(True),
                                        second.splitlines(True)))
        if msg:
            message += " : " + msg
        pytest.fail("Multi-line strings are unequal:\n" + message)


def assertFileHeadLines(filename, lines):
    """Assert that first few lines in the file with given name are equal to given lines.
    If they aren't, show a nice diff.
    None entry in lines will be skipped.
    """
    __tracebackhide__ = True

    if not lines:
        return

    orig_len = len(lines)
    with Path(filename).open() as f:
        def skip_none(fline, line):
            if line is None:
                line = fline
            return (fline, line)
        flines, lines = zip(*[skip_none(fline, line) for fline, line in zip(f, lines)])
        assert len(flines) == orig_len
    return assertMultiLineEqual(''.join(flines), ''.join(lines))


def assertFileStructure(basedir, manifest):
    """Assert that the file system structure starting from basedir follows the manifest.
    Only paths in the manifest are checked.
    """
    __tracebackhide__ = True

    basedir = Path(basedir)
    for relpath in manifest:
        path = basedir / relpath
        if relpath.endswith('/'):
            assert path.is_dir()
        else:
            assert path.is_file()
