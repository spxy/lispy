run: FORCE
	uv run lis.py

lint: FORCE
	uv run ruff check
	uv run ruff format --diff
	uv run mypy .

test: FORCE
	uv run -m pytest -v

chk: lint test
	uv run -m pytest -vv

fix: FORCE
	uv run ruff format
	uv run ruff check --fix

deps: FORCE
	curl -LsSf https://astral.sh/uv/install.sh | sh

norvig: FORCE
	mkdir -p norvig/
	# Wed, 24 Oct 2018
	curl -sS https://raw.githubusercontent.com/norvig/pytudes/ebda293/py/lis.py -o norvig/lis.py
	# Wed, 17 Oct 2018
	curl -sS https://raw.githubusercontent.com/norvig/pytudes/6a8e87e/py/lispy.py -o norvig/lispy.py

run-norvig-lispy: FORCE
	uv run python3 -c "from norvig.lis import repl; repl()"

FORCE:
