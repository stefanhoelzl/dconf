# type: ignore
# pylint: disable=all
from invoke import task


@task
def fmt(c):
    c.run("isort .")
    c.run("black .")


@task
def test(c):
    c.run("pytest", pty=True)
