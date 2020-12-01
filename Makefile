.PHONY: tests

install:
	pipenv install --dev

update:
	pipenv clean
	pipenv upgrade --dev

test:
	pipenv run pytest --cov=aoc

tests: test

flake8:
	pipenv run flake8 aoc tests

black:
	pipenv run black --check --diff aoc tests

check: flake8 black
