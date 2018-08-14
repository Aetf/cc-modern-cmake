from __future__ import print_function, absolute_import, division

from invoke import task


@task(default=True)
def init(c):
    """Initialize and install dependencies"""
    c.run("pip install pipenv")
    c.run("pipenv install")


@task
def test(c, pytestArgs=''):
    """Run tests"""
    test_cmd = ['pipenv', 'run', 'pytest', 'tests', pytestArgs]
    c.run(' '.join(test_cmd), pty=True)


@task
def bump_version(c):
    """Bump version"""
    pass

@task
def release(c):
    """Do a release"""
    pass
