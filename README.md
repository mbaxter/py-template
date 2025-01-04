# Python Template Project

## Initialize New Project from Template
**Important**: For regular projects that have already been initialized, these instructions don't apply.

Template setup instructions:
1. Set your Python version:
   - Set version in `.python-version`
   - Update Python version constraints in `pyproject.toml`:
     ```toml
     [tool.poetry.dependencies]
     python = "^3.10,<3.12"  # Update this line
     
     [tool.ruff]
     target-version = "py310"  # Update this line
     ```
   - Update GitHub Actions Python version in `.github/workflows`

2. Update project metadata in `pyproject.toml`:
   ```toml
   [tool.poetry]
   name = "your-project-name"
   version = "0.1.0"
   description = "Your project description"
   authors = ["Your Name <your.email@example.com>"]
   ```

3. Rename `package_name` directory to match your project name

4. Update README:
   - Change the project title at the top
   - Remove this "Initialize New Project from Template" section when done

5. Follow setup instructions below

## Local Development

### Setup

1. **Install Python**
   ```shell
   # Install pyenv if you haven't already: https://github.com/pyenv/pyenv#getting-pyenv
   pyenv install $(cat .python-version)
   ```

2. **Install Poetry**
   ```shell
   # Install pipx if you haven't already: https://pipx.pypa.io/latest/installation/
   pipx install poetry
   
   # Configure Poetry
   poetry config virtualenvs.prefer-active-python true
   poetry config virtualenvs.in-project true
   ```

3. **Setup Project**
   ```shell
   poetry install  # Install dependencies and create virtualenv
   poetry update  # Update dependencies to latest compatible versions
   poetry shell   # Activate virtualenv
   pre-commit install  # Setup git hooks
   ```

### Development Tools

All code quality tools run automatically on commit via pre-commit hooks:
- **Black**: Code formatting
- **Ruff**: Fast Python linter
- **MyPy**: Static type checking
- **Pytest**: Testing (including doctests)
- **Safety**: Dependency vulnerability checking
- **Bandit**: Security linting

To run tools manually:
```shell
# Testing
pytest

# Linting/Formatting (only needed if you want to run before committing)
black .
ruff check --fix .
mypy .
bandit -r .
safety check
```

### Virtual Environment
```shell
poetry shell  # Activate
exit         # Deactivate
```

### Managing Dependencies
```shell
# Add dependencies
poetry add <package>              # Regular dependency
poetry add --group=dev <package>  # Development dependency
poetry add --group=test <package> # Test dependency

# Update dependencies
poetry update  # Update all dependencies
poetry update <package>  # Update specific package
```
