from __future__ import print_function, division, absolute_import

import sys
import pytest

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path


@pytest.fixture
def mock_context():
    """Returns a mock extra_context for cookiecutter
    """
    context = {
        "full_name": "Test Name",
        "email": "test@example.com",
        "obs_email": "test at example dot com",
        "github_username": "testgh",
        "project_name": "Test project",
        "project_short_description": "A short description of the project",
        "version": "0.1.0",
        "with_qt": True
    }
    return context


@pytest.fixture
def mock_project_manifest():
    """Returns a mock project manifest for cookiecutter
    """
    return [
        '.gitmodules',
        '.gitignore',
        'CHANGELOG.md',
        'README.md',
        'LICENSE',
        'VERSION',
        'tasks.py',
        'cmake/',
        'include/',
        'src/',
        'thirdparty/',
        'tests/',
    ]


def find_ext_dir():
    # Walk up from current file until we have the cookiecutter.json file
    for repodir in Path(__file__).absolute().parents:
        if (repodir / 'cookiecutter.json').exists():
            extdir = repodir / 'extensions'
            if extdir.is_dir():
                return extdir
    return None


def pytest_runtest_setup(item):
    # A hack to load local Jinja extensions.
    # When cookiecutter is called from commandline, there is an active Click
    # context and thus cookiecutter_repo_extensions.Extension can detect the repo
    # root and setup sys.path accordingly.
    # But when cookiecutter is called from tests, there is no active Click
    # context so we have to setup the sys.path ourselves.

    extdir = find_ext_dir()
    if extdir is None:
        return

    # save old sys.path
    item.old_syspath = sys.path.copy()

    try:
        sys.path.remove(str(extdir))
    except ValueError:
        pass
    sys.path.insert(0, str(extdir))


def pytest_runtest_teardown(item, nextitem):
    try:
        sys.path = item.old_syspath
    except AttributeError:
        pass
