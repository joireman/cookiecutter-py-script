# tasks.py - Requires 'invoke' to be installed
from invoke import task

@task(help={'clean': "removes virtual environment"})
def install(ctx, clean=False):
    """Create virtual env and install dependencies from lockfile."""
    if clean:
        ctx.run("rm -rf .venv")

    # uv is called globally
    ctx.run("rm -f uv.lock")
    ctx.run("uv venv --clean")
    ctx.run("uv sync")

@task
def dev(ctx):
    # uv is called globally
    ctx.run("rm -f uv.lock")
    ctx.run("uv venv --clean")
    ctx.run("uv lock")
    ctx.run("uv --extra dev")

@task
def test(ctx):
    """Run tests with pytest."""
    # Note: Invoke automatically finds the venv's Python when calling Python scripts
    ctx.run(".venv/Scripts/python.exe -m pytest")

@task 
def lint(ctx):
    ctx.run(".venv/Scripts/python.exe -m ruff check .")

@task 
def coverage(ctx):
    ctx.run("open htmlcov/index.html.")

@task 
def typecheck(ctx):
    ctx.run(".venv/Scripts/python.exe -m mypy .")

@task 
def security(ctx):
    ctx.run(".venv/Scripts/python.exe -m bandit -r .")

@task 
def format(ctx):
    ctx.run(".venv/Scripts/python.exe -m ruff format .")
    ctx.run(".venv/Scripts/python.exe -m ruff check --fix .")

@task
def docs(ctx):
    ctx.run(".venv/Scripts/python.exe -m mkdocs serve")
