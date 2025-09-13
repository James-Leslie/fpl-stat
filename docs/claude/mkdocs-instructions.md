For documentation, we use Material for MkDocs. The documentation source files are located in @docs/

# Installation
MkDocs, and all of the necessary plugin dependencies, are installed as dev dependencies and managed via `uv`.

# Configuration
The MkDocs configuration is in @mkdocs.yml. This file defines site settings, theme configuration, navigation structure, and plugins.

## Plugins
We use the following MkDocs plugins:
  - search: Provides search functionality for the documentation
  - mkdocstrings: Automatically generates API documentation from docstrings in the codebase
  - mkdocs-jupyter: Integrates Jupyter Notebooks into the documentation

For more information about Material for MkDocs, please refer to the official documentation at https://squidfunk.github.io/mkdocs-material

# Building the documentation
To build the documentation locally, run `uv run mkdocs build`. To serve the documentation locally with live reloading, run `uv run mkdocs serve`.

# Deployment
The documentation is hosted in GitHub Pages, and is deployed automatically via GitHub Actions on push to the `main` branch. The deployment action is found at @.github/workflows/deploy-docs.yml