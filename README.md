# Odoo Pre-commit Hooks

This repo provides pre-commit hooks for Odoo development:

- Ensures all Python files have `# -*- coding: utf-8 -*-` at the top.
- Ensures all JS files have `/** @odoo-module */` at the top.
- Removes `print(...)` from Python and `console.log(...)` from JavaScript files.

## Usage

In your Odoo project, add this to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/PrakashSuthar7664/odoo-precommit-hooks.git
    rev: v1.0.4
    hooks:
      - id: add-python-utf8-header
      - id: add-js-odoo-header
      - id: remove-debug-statements
