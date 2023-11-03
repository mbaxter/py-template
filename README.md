# Python Template Project

## Initialize New Project from Template
**Important**: For regular projects that have already been initialized, these instructions don't apply.

Template setup instructions:
- Update the python version if necessary:
  - Update `.python-version` to set your project's python version.
  - Update "target-version" in `pyproject.toml`. This field is used by tools like `ruff` (a linter) to determine what language features to support.  Set this to match `.python-version` or set it to a lower value for greater backwards compatibility.
- Make sure [pyenv](https://github.com/pyenv/pyenv#getting-pyenv) is installed on your machine.
- Run code below to initialize project:
  - ```shell
    pyenv install $(cat .python-version)
    python3 -m venv venv
    source venv/bin/activate
    ./venv/bin/pip install pip-tools
    pip-compile
    pip-sync
    ```
- Change folder "package_name" to match your project name
- Update README title
- Remove this section from README

Install git hooks:
```shell
pre-commit install
```

## Local Development

### Testing
To run unit tests:
```shell
pytest
```

### Setup

Manage python version with [pyenv](https://github.com/pyenv/pyenv#getting-pyenv).
Just install pyenv and make sure you have the correct python version installed before setting up your virtual env below:

```shell
pyenv install $(cat .python-version)
```

Setup your venv and install requirements:
```shell
python3 -m venv venv
source venv/bin/activate
./venv/bin/pip install -r requirements.txt
```

Install git hooks:
```shell
pre-commit install
```

Deactivate your venv:
```shell
deactivate
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

### Managing dependencies with pip-tools

Save updated requirements:
```shell
pip-compile
```

Update env:
```shell
pip-sync
```

Update requirements:
```shell
pip-compile --upgrade
```

Update a specific package:
```shell
pip-compile --upgrade-package <pkg-name>
```