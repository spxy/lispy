run:
	./lispy.py

check:
	uv run ruff check
	uv run ruff format --diff
	uv run mypy .
	uv run -m pytest

fix:
	uv run ruff format
	uv run ruff check --fix

deps:
	curl -LsSf https://astral.sh/uv/install.sh | sh
