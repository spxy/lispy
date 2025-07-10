run: FORCE
	uv run lispy.py

lint: FORCE
	uv run ruff check
	uv run ruff format --diff
	uv run mypy .

test: FORCE
	uv run -m pytest -v

check: lint test
	uv run -m pytest -vv

fix: FORCE
	uv run ruff format
	uv run ruff check --fix

deps: FORCE
	curl -LsSf https://astral.sh/uv/install.sh | sh

FORCE:
