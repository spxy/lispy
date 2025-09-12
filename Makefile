help:
	@echo 'Usage: make [target]'
	@echo
	@echo 'Targets to run Lispy:'
	@echo "  lis    Run Susam's Simple Lispy."
	@echo "  nlis   Run Norvig's Simple Lispy."
	@echo
	@echo 'Targets to run checks:'
	@echo '  lint   Run linters.'
	@echo '  test   Run tests.'
	@echo '  chk    Run both linters and tests.'
	@echo '  fix    Fix lints.'
	@echo
	@echo 'Targets to set up development environment:'
	@echo '  deps   Install uv.'
	@echo "  dl     Download Norvig's Lispy programs."


# Run
# ---

lis: FORCE
	uv run lis.py

nlis: FORCE
	uv run python3 -c "from norvig.lis import repl; repl()"

lint: FORCE
	uv run ruff check
	uv run ruff format --diff
	uv run mypy .


# Checks
# ------

test: FORCE
	uv run -m pytest -v

checks: lint test
	uv run -m pytest -vv

fix: FORCE
	uv run ruff format
	uv run ruff check --fix


# Development Environment Setup
# -----------------------------

deps: FORCE
	curl -LsSf https://astral.sh/uv/install.sh | sh

dl: FORCE
	mkdir -p norvig/
	# Wed, 24 Oct 2018
	curl -sS https://raw.githubusercontent.com/norvig/pytudes/ebda293/py/lis.py -o norvig/lis.py
	# Wed, 17 Oct 2018
	curl -sS https://raw.githubusercontent.com/norvig/pytudes/6a8e87e/py/lispy.py -o norvig/lispy.py

FORCE:
