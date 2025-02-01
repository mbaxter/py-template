# Python Template Project

## Initialize New Project from Template
**Important**: For regular projects that have already been initialized, these instructions don't apply.

### Quick Setup (Recommended)
Run the interactive setup script:
```shell
python init_project.py
```

The script will guide you through:
- Setting project name and metadata
- Choosing Python version
- Setting up author information
- Selecting a license (optional)

### Manual Setup (Alternative)
If you prefer to set up manually, follow these steps:

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

5. Choose a license (optional):
   - Visit [choosealicense.com](https://choosealicense.com/) to select a license
   - Add the license text to a LICENSE file

After either setup method, proceed to the Development Setup below.

## Local Development

### Prerequisites
This project uses pyenv for Python version management and Poetry for dependency management.

Install pyenv:
- Follow the installation guide at https://github.com/pyenv/pyenv#getting-pyenv

Install and configure Poetry:
```shell
pipx install poetry
poetry config virtualenvs.prefer-active-python true
poetry config virtualenvs.in-project true
```

### Project Setup

Install Project Python Version:
```shell
pyenv install $(cat .python-version)
```

Setup Development Environment:
Install dependencies, update to latest compatible versions, activate virtualenv, and set up git hooks:
```shell
poetry install
poetry update
poetry shell
pre-commit install
```

### Development Tools

All code quality tools run automatically on commit via pre-commit hooks:
- **Black**: Code formatting
- **Ruff**: Fast Python linter
- **MyPy**: Static type checking
- **Pytest**: Testing (including doctests)

To run tools manually:
```shell
# Run all checks
pre-commit run --all-files

# Or run individual tools
pre-commit run black --all-files
pre-commit run ruff --all-files
pre-commit run mypy --all-files

# Only pytest needs to run directly since it uses the project environment
pytest
```

### Virtual Environment

```shell
poetry shell  # Activate virtualenv
exit          # Deactivate virtualenv
```

### Managing Dependencies

Add new dependencies:
```shell
poetry add <package>              # Add regular dependency
poetry add --group=dev <package>  # Add dev dependency
poetry add --group=test <package> # Add test dependency
```

Update dependencies:
```shell
poetry update           # Update all dependencies
poetry update <package> # Update a specific dependency
```
