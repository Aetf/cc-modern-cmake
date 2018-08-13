from __future__ import print_function, division, absolute_import
from contextlib import contextmanager

import os
import subprocess as sp


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    result = cookies.bake(extra_context={'project_slug': 'test_project'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'test_project'
    assert result.project.isdir()


def test_run_flake8(cookies):
    result = cookies.bake(extra_context={'project_slug': 'flake8_compat'})
    with inside_dir(str(result.project)):
        assert sp.check_call(['flake8']) == 0
