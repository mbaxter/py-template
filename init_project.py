#!/usr/bin/env python3
"""Interactive script to initialize a new project from the template."""

import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional
import urllib.request
import json

PYTHON_VERSIONS = ["3.8", "3.9", "3.10", "3.11", "3.12"]
LICENSE_OPTIONS = {
    "mit": "MIT License - Simple and permissive",
    "apache-2.0": "Apache License 2.0 - Patent protection and trademark use",
    "gpl-3.0": "GNU GPLv3 - Copyleft requiring source distribution",
    "bsd-3-clause": "BSD 3-Clause - Similar to MIT but with an extra clause",
    "none": "No License - All rights reserved",
}

# GitHub's API endpoint for license templates
GITHUB_LICENSE_API = "https://api.github.com/licenses/{}"
GITHUB_API_HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "Python-Project-Template",
}


@dataclass
class ProjectConfig:
    """Configuration for a new project."""
    name: str
    description: str
    author_name: str
    author_email: str
    python_version: str
    license_type: str


def get_valid_project_name(name: str) -> Optional[str]:
    """Validate and format project name."""
    # Convert to lowercase and replace spaces/hyphens with underscores
    name = re.sub(r"[-\s]+", "_", name.lower())
    
    # Check if it's a valid Python package name
    if not re.match(r"^[a-z][a-z0-9_]*$", name):
        return None
    return name


def fetch_license_text(license_key: str, author_name: str) -> Optional[str]:
    """Fetch license text from GitHub API and format it."""
    try:
        url = GITHUB_LICENSE_API.format(license_key)
        request = urllib.request.Request(url, headers=GITHUB_API_HEADERS)
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read())
            
            # Get the license text and replace placeholders
            text = data["body"]
            year = str(datetime.now().year)
            text = text.replace("[year]", year)
            text = text.replace("[yyyy]", year)
            text = text.replace("[fullname]", author_name)
            text = text.replace("[name of copyright owner]", author_name)
            return text
    except Exception as e:
        print(f"Warning: Could not fetch license text: {e}")
        return None


def prompt_project_config() -> ProjectConfig:
    """Prompt user for project configuration."""
    print("\n=== Python Project Initialization ===\n")
    
    # Project name
    while True:
        name = input("Project name: ").strip()
        valid_name = get_valid_project_name(name)
        if valid_name:
            break
        print("Invalid project name. Use only letters, numbers, and underscores. Must start with a letter.")
    
    # Basic info
    description = input("Project description: ").strip()
    author_name = input("Author name: ").strip()
    author_email = input("Author email: ").strip()
    
    # Python version
    print("\nAvailable Python versions:")
    for i, version in enumerate(PYTHON_VERSIONS, 1):
        print(f"{i}. {version}")
    while True:
        try:
            choice = int(input("\nChoose Python version (enter number): "))
            python_version = PYTHON_VERSIONS[choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a number from the list.")
    
    # License
    print("\nAvailable licenses:")
    for key, desc in LICENSE_OPTIONS.items():
        print(f"- {key}: {desc}")
    while True:
        license_type = input("\nChoose license (enter key): ").lower()
        if license_type in LICENSE_OPTIONS:
            break
        print("Invalid choice. Please enter one of the listed keys.")
    
    return ProjectConfig(
        name=valid_name,
        description=description,
        author_name=author_name,
        author_email=author_email,
        python_version=python_version,
        license_type=license_type,
    )


def update_python_version(config: ProjectConfig) -> None:
    """Update Python version in relevant files."""
    # Update .python-version
    with open(".python-version", "w") as f:
        f.write(config.python_version)
    
    # Update pyproject.toml
    with open("pyproject.toml", "r") as f:
        content = f.read()
    
    # Update Python dependency version
    content = re.sub(
        r'python = "\^[0-9.]+,<[0-9.]+"',
        f'python = "^{config.python_version},<{float(config.python_version) + 0.1:.1f}"',
        content
    )
    
    # Update ruff target version
    content = re.sub(
        r'target-version = "py\d+"',
        f'target-version = "py{config.python_version.replace(".", "")}"',
        content
    )
    
    with open("pyproject.toml", "w") as f:
        f.write(content)


def update_project_metadata(config: ProjectConfig) -> None:
    """Update project metadata in pyproject.toml."""
    with open("pyproject.toml", "r") as f:
        content = f.read()
    
    # Update project metadata
    content = re.sub(r'name = "package-name"', f'name = "{config.name}"', content)
    content = re.sub(r'description = ""', f'description = "{config.description}"', content)
    content = re.sub(
        r'#\s*"Author Name <author-email@domain.com>",',
        f'    "{config.author_name} <{config.author_email}>",',
        content
    )
    
    with open("pyproject.toml", "w") as f:
        f.write(content)


def rename_package_directory(config: ProjectConfig) -> None:
    """Rename the package directory to match project name."""
    os.rename("package_name", config.name)


def update_readme(config: ProjectConfig) -> None:
    """Update README.md with project name and remove template instructions."""
    with open("README.md", "r") as f:
        content = f.read()
    
    # Update title
    content = re.sub(r"# Python Template Project", f"# {config.name}", content)
    
    # Remove template instructions section
    content = re.sub(
        r"## Initialize New Project from Template.*?(?=## Local Development)",
        "",
        content,
        flags=re.DOTALL,
    )
    
    with open("README.md", "w") as f:
        f.write(content)


def handle_license(config: ProjectConfig) -> None:
    """Handle license file based on user choice."""
    if config.license_type == "none":
        return
    
    license_text = fetch_license_text(config.license_type, config.author_name)
    if license_text:
        with open("LICENSE", "w") as f:
            f.write(license_text)
        print("\nLicense file created successfully.")
    else:
        print("\nWarning: Could not create license file automatically.")
        print(f"Please visit https://choosealicense.com/licenses/{config.license_type}/ to get the license text.")


def main() -> None:
    """Main initialization function."""
    if not all(os.path.exists(f) for f in ["pyproject.toml", "package_name", "README.md"]):
        print("Error: Must be run from the template root directory")
        sys.exit(1)
    
    config = prompt_project_config()
    
    print("\nInitializing project...")
    update_python_version(config)
    update_project_metadata(config)
    rename_package_directory(config)
    update_readme(config)
    handle_license(config)
    
    print("\nSetup successfully completed. Removing init_project.py script...")
    
    # Delete this script
    try:
        os.remove(__file__)
    except Exception as e:
        print(f"Warning: Could not remove setup script: {e}")
        print("You may want to delete init_project.py manually.")
    
    print("\nNext steps:")
    if config.license_type != "none":
        print("1. Review the generated license file")
    print("2. Initialize a new git repository")
    print("3. Follow the setup instructions in README.md")


if __name__ == "__main__":
    main() 