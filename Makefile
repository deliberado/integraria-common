.PHONY: venv install test lint fmt

venv:
	uv venv

install:
	uv pip install -e ".[dev]" || true
	uv pip install -e .

test:
	uv run pytest

lint:
	uv run python -m compileall src

fmt:
	@echo "No formatter configured. Add ruff/black if desired."
