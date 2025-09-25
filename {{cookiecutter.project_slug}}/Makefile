.PHONY: install format lint test security

VENV_DIR := .venv
PYTHON_BIN := $(VENV_DIR)/bin/python

install:
	uv venv
	uv pip install -e ".[dev]"
	uv pip compile --output-file uv.lock --extra dev pyproject.toml
	uv pip sync uv.lock

format:
	$(PYTHON_BIN) -m ruff format .
	$(PYTHON_BIN) -m ruff check --fix .

lint:
	$(PYTHON_BIN) -m ruff check .

test:
	$(PYTHON_BIN) -m pytest

coverage:
	open htmlcov/index.html

typecheck:
	$(PYTHON_BIN) -m mypy .

security:
	$(PYTHON_BIN) -m bandit -r .
