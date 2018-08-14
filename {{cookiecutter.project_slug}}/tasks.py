from __future__ import print_function, absolute_import, division

from invoke import task


@task()
def init(c):
    """Initialize and install dependencies"""
    pass


@task
def configure(c, cmakeArgs='', buildDir='build'):
    """Configure using cmake"""
    cmake_cmd = ['cmake', '-H', '.', '-B', buildDir, cmakeArgs]
    c.run(' '.join(cmake_cmd))


@task(default=True)
def build(c, cmakeArgs='', buildDir='build'):
    """Build the project"""
    cmake_cmd = ['cmake', '--build', buildDir, cmakeArgs]
    c.run(' '.join(cmake_cmd))


@task
def test(c):
    """Run tests"""
    pass


@task
def bump_version(c):
    """Bump version"""
    pass


@task
def release(c):
    """Do a release"""
    pass
