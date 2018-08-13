from __future__ import print_function, absolute_import, division

from invoke import task


@task(default=True)
def init(c):
    """Initialize and install dependencies"""
    c.run("pip install pipenv")
    c.run("pipenv install")


@task
def test(c):
    """Run tests"""
    c.run("pipenv run pytest tests")


@task
def bump_version(c):
    """Bump version"""
    pass

@task
def release(c):
    """Do a release"""
    pass
