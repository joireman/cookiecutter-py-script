{% if cookiecutter.include_mkdocs_docs.lower() == 'yes' %}
.PHONY: install format lint test security help typecheck all clean coverage docs dev audit
{% else %}
.PHONY: install format lint test security help typecheck all clean coverage dev audit
{% endif %}

VENV_DIR := .venv
PYTHON_BIN := $(VENV_DIR)/bin/python

help:
	@echo "Available commands:"
	@echo "  all       - Run format, lint, and test"
	@echo "  audit     - Runs py-audit (must be installed globally)"
	@echo "  clean     - Remove temporary Python files"
	@echo "  dev       - Create virtual env and install runtime and development dependencies from lockfile"
	@echo "  coverage  - Open a browser to view coverage HTML report"
{% if cookiecutter.include_mkdocs_docs.lower() == 'yes' %}
	@echo "  docs      - Serve documentation locally"
{% endif %}
	@echo "  format    - Auto-format code using Ruff"
	@echo "  install   - Create virtual env and install runtime dependencies from lockfile"
	@echo "  lint      - Check code for style issues and errors using Ruff"
	@echo "  security  - Run security checks with Bandit"
	@echo "  test      - Run tests with pytest and generate coverage report"
	@echo "  typecheck - Run type checks with mypy"

install:
	rm -f uv.lock
	uv venv --clean
	uv sync 

audit: 
	pip-audit

dev:
	rm -f uv.lock
	uv venv --clean
	uv lock 
	uv sync --extra dev 

format:
	$(PYTHON_BIN) -m ruff format .
	$(PYTHON_BIN) -m ruff check --fix .
{% if cookiecutter.include_mkdocs_docs.lower() == 'yes' %}
docs:
	$(PYTHON_BIN) -m mkdocs serve
{% endif %}
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

all: format lint test

# Cleanup
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache .coverage
