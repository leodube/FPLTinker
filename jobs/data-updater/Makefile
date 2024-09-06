PROJECT_NAME:=data_updater

################################################################################
# COMMANDS -- Setup                                                            #
################################################################################
setup: clean install

clean: clean-pyc clean-test ## Clean the project
	rm -rf .venv/

clean-pyc: ## Clean cache files
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## clean test files
	find . -name '.pytest_cache' -exec rm -fr {} +
	rm -f .coverage
	rm -fr htmlcov/

install:
	poetry install

run:
	. .venv/bin/activate && python update.py


################################################################################
# COMMANDS -- CI                                                               #
################################################################################
format:
	. .venv/bin/activate && isort $(PROJECT_NAME) tests && black $(PROJECT_NAME) tests

pylint:
	. .venv/bin/activate && --rcfile=setup.cfg pylint $(PROJECT_NAME) tests

flake8:
	. .venv/bin/activate && flake8 $(PROJECT_NAME) tests

lint: pylint flake8

test:
	. .venv/bin/activate && pytest
