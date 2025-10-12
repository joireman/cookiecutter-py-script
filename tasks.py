# tasks.py - Requires 'invoke' to be installed
from invoke import task

@task(help={'clean': "removes virtual environment before starting."})
def install(ctx, clean=False):
    """Create virtual env and install dependencies from lockfile."""
    if clean:
        ctx.run("rm -rf .venv")

    # uv is called globally
    ctx.run("uv venv")
    ctx.run("uv pip install -e \".[dev]\"")
    ctx.run("uv pip compile --output-file uv.lock --extra dev --extra analysis pyproject.toml")
    ctx.run("uv pip sync uv.lock")

@task
def test(ctx):
    """Run tests with pytest."""
    # Note: Invoke automatically finds the venv's Python when calling Python scripts
    ctx.run(".venv/Scripts/python.exe -m pytest")

@task 
def lint(ctx):
    ctx.run(".venv/Scripts/python.exe -m ruff check .")

@task 
def docs(ctx):
    ctx.run("open htmlcov/index.html.")

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
