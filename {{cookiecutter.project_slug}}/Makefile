.PHONY: install format lint test security

install:
	uv pip install --no-deps -e .
	uv pip compile --no-emit-hashes pyproject.toml --output-file uv.lock
	uv pip sync uv.lock

format:
	uv run ruff check --fix .
	uv run ruff format .

lint:
	uv run ruff check .

test:
	uv run pytest

security:
	uv run bandit -r .
