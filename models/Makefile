PROJECT_NAME:=models

# Load .env
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

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


################################################################################
# COMMANDS -- CI                                                               #
################################################################################
format:
	. .venv/bin/activate && isort $(PROJECT_NAME) tests && black $(PROJECT_NAME) tests

pylint:
	. .venv/bin/activate && pylint --rcfile=setup.cfg $(PROJECT_NAME) tests

flake8:
	. .venv/bin/activate && flake8 $(PROJECT_NAME) tests

lint: pylint flake8

test:
	. .venv/bin/activate && pytest

################################################################################
# COMMANDS -- Migrations                                                       #
################################################################################
create-db:
	createdb \
	-h $(DATABASE_HOST) \
	-p $(DATABASE_PORT) \
	-U $(DATABASE_USERNAME) \
	-T template0 \
	$(DATABASE_NAME)

db-init:
	flask db init

db-migrate:
	flask db migrate

db-upgrade:
	flask db upgrade
