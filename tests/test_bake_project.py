from __future__ import print_function, division, absolute_import

import subprocess as sp
from datetime import datetime

from helpers import (inside_dir, assertFileHeadLines, cast_path, assertFileStructure)


def test_project_tree(cookies, mock_context, mock_project_manifest):
    result = cookies.bake(extra_context=mock_context)
    assert result.exit_code == 0
    assert result.exception is None

    project = cast_path(result.project)
    assert project.name == 'test-project'
    assert project.is_dir()

    assertFileHeadLines(project/'VERSION', [mock_context['version']])
    assertFileHeadLines(project/'LICENSE', [
        None, None,
        "Copyright (c) {year} {full_name} <{obs_email}>\n".format(year=datetime.now().year, **mock_context)
    ])

    assertFileStructure(project, mock_project_manifest)


def test_project_build(cookies, mock_context):
    result = cookies.bake(extra_context=mock_context)
    assert result.exit_code == 0

    project = cast_path(result.project)
    with inside_dir(project):
        assert sp.check_call(['mkdir', '-p', 'build']) == 0
        assert sp.check_call(['cmake', '-H.', '-Bbuild']) == 0
        assert sp.check_call(['cmake', '--build', 'build']) == 0


def test_run_flake8(cookies, mock_context):
    result = cookies.bake(extra_context=mock_context)
    assert result.exit_code == 0

    project = cast_path(result.project)
    with inside_dir(project):
        assert sp.check_call(['flake8']) == 0
