PROJECT_NAME:=api

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
	. .venv/bin/activate && python -m flask run -p 5000


################################################################################
# COMMANDS -- CI                                                               #
################################################################################
format:
	. .venv/bin/activate && isort $(PROJECT_NAME) && black $(PROJECT_NAME)

pylint:
	. .venv/bin/activate && pylint $(PROJECT_NAME)

flake8:
	. .venv/bin/activate && flake8 $(PROJECT_NAME)

lint: pylint flake8