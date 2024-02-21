# Python Template Project

## Initialize New Project from Template
**Important**: For regular projects that have already been initialized, these instructions don't apply.

Template setup instructions:
- Update the python version if necessary:
  - Update `.python-version` to set your project's python version.
  - Update "target-version" in `pyproject.toml`. This field is used by tools like `ruff` (a linter) to determine what language features to support.  Set this to match `.python-version` or set it to a lower value for greater backwards compatibility.
  - Update `tool.poetry.dependencies.python` variable in `pyproject.toml`
  - Update `[.pre-commit-config.yaml](.pre-commit-config.yaml)` "language_version" variable
  - Update your [/.github/workflows](./.github/workflows) `matrix.python-version` arrays
- Update project variables `pyproject.toml`:
  - Set project `name` variable
  - Set project `description` variable
  - Set project `version` variable
  - Set project `authors` variable
- Change folder "package_name" to match your project name
- Update README title
- Follow the instructions in the [Setup section](#setup)
- Remove this section from README

## Local Development

### Setup

#### Python
Manage python version with [pyenv](https://github.com/pyenv/pyenv#getting-pyenv).
Just install pyenv and make sure you have the correct python version installed before setting up your virtual env below:

```shell
pyenv install $(cat .python-version)
```
#### Dependencies
Make sure you have poetry installed:
- Poetry can be installed via [pipx](https://pipx.pypa.io/latest/installation/)
- Install poetry with: `pipx install poetry`

Set the poetry config with:
```shell
poetry config virtualenvs.prefer-active-python true
poetry config virtualenvs.in-project true
```
The `prefer-active-python` setting tells poetry to use the version of python currently active in the shell.  This will ensure that your `pyenv` python version is respected by poetry.
The `virtualenvs.in-project` setting tells poetry to save your virtual env within your project instead of in a global cache.

Setup your venv and install requirements:
```shell
poetry shell
poetry install
poetry upgrade
```

#### Dev environment
Install git hooks:
```shell
pre-commit install
```

### Testing
To run unit tests:
```shell
pytest
```

### Virtual env ###
Use poetry to manage your virtual env

Activate your venv with:
```shell
poetry shell
```

Deactivate your venv with:
```shell
exit
```

### Linter ###
To check linting rules:
```shell
ruff check .
```

To automatically fix linting issues where possible:
```shell
ruff check --fix . 
```

### Code Formatter ###
```shell
black .
```

### Managing dependencies with poetry

Add dependencies:
```shell
poetry add <dep1> <dep2>
```

Add a dev dependency:
```shell
poetry add --group=dev <dep>
```

Add a test dependency:
```shell
poetry add --group=test <dep>
```

Update a dependency:
```shell
poetry upgrade <dep>
```

Update all dependencies:
```shell
poetry upgrade
```
