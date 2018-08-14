from __future__ import print_function, division, absolute_import

import subprocess as sp

from helpers import cast_path, inside_dir


def test_project_configure(cookies, mock_context):
    result = cookies.bake(extra_context=mock_context)
    assert result.exit_code == 0

    project = cast_path(result.project)

    with inside_dir(project):
        assert sp.check_call(['inv', 'configure', '--buildDir', 'build/another', '-DCUSTOM_VAR=value']) == 0
        buildDir = project/'build'/'another'
        assert buildDir.is_dir()

        with inside_dir(buildDir):
            outputs = sp.check_output(['cmake', '-L', str(project)], universal_newlines=True).split('\n')
            assert 'CUSTOM_VAR:STRING=value' in outputs


def test_project_build(cookies, mock_context):
    result = cookies.bake(extra_context=mock_context)
    assert result.exit_code == 0

    project = cast_path(result.project)

    with inside_dir(project):
        assert sp.check_call(['inv', 'build', '--buildDir', 'build/another']) == 0
        buildDir = project/'build'/'another'
        assert buildDir.is_dir()
