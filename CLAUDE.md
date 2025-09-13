# Summary
Python package for loading and transforming Fantasy Premier League API data.

# Tooling & Methodology
- **Package management**: UV only (never pip/conda)
- **Testing**: pytest with high coverage
- **Documentation**: MkDocs + GitHub Pages
- **Release**: Semantic versioning via GitHub releases

# Code Standards
- Type hints and Google-style docstrings required
- Use f-strings, follow PEP 8
- Self-documenting code with clear naming

# Key Commands
```bash
uv add package-name              # Add dependencies
uv run pytest                    # Run tests
uv run mkdocs serve              # Preview docs
uv version --bump patch          # Version bump
uvx pre-commit run --all-files   # Manual quality check
```

# Essential Rules
- **Always use UV** for dependency management (never edit pyproject.toml manually)
- **Frequent commits** with descriptive messages
- **Pre-commit hooks** prevent low-quality commits
- **GitHub CLI preferred** for git operations

# CLAUDE.md Maintenance
**IMPORTANT**: This CLAUDE.md file should be kept up-to-date as the project evolves. When making significant changes to tooling, workflows, or project structure, update the relevant sections in this file. This ensures future AI assistance remains consistent with project conventions.