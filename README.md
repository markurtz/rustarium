<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/markurtz/rustarium/main/docs/assets/branding/logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/markurtz/rustarium/main/docs/assets/branding/logo-light.svg">
    <img alt="rustarium Logo" src="https://raw.githubusercontent.com/markurtz/rustarium/main/docs/assets/branding/logo-light.svg" width="400">
  </picture>
</p>

<p align="center">
  <em>A high-performance, telemetrized process orchestrator and sandbox for Python and WASM, forged in Rust.</em>
</p>

<p align="center">
  <!-- Package & Release Status -->
  <a href="https://github.com/markurtz/rustarium/releases">
    <img src="https://img.shields.io/github/v/release/markurtz/rustarium?label=Release" alt="GitHub Release">
  </a>
  <a href="https://pypi.org/project/rustarium/">
    <img src="https://img.shields.io/pypi/v/rustarium?label=PyPI" alt="PyPI Release">
  </a>
  <a href="https://pypi.org/project/rustarium/">
    <img src="https://img.shields.io/pypi/pyversions/rustarium?label=Python" alt="Supported Python Versions">
  </a>
  <br/>
  <!-- CI/CD & Build Status -->
  <a href="https://github.com/markurtz/rustarium/actions/workflows/main.yml">
    <img src="https://github.com/markurtz/rustarium/actions/workflows/main.yml/badge.svg" alt="CI Status">
  </a>
  <br/>
  <!-- Issues & Support -->
  <a href="https://github.com/markurtz/rustarium/issues?q=is%3Aissue+is%3Aclosed">
    <img src="https://img.shields.io/github/issues-closed/markurtz/rustarium?label=Issues%20Closed" alt="Closed Issues">
  </a>
  <a href="https://github.com/markurtz/rustarium/issues?q=is%3Aissue+is%3Aopen">
    <img src="https://img.shields.io/github/issues/markurtz/rustarium?label=Issues%20Open" alt="Open Issues">
  </a>
  <a href="https://opensource.org/licenses/Apache-2.0">
    <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License">
  </a>
</p>

<p align="center">
  <a href="https://markurtz.github.io/rustarium/">Documentation</a> |
  <a href="https://github.com/markurtz/rustarium/milestones">Roadmap</a> |
  <a href="https://github.com/markurtz/rustarium/issues">Issues</a> |
  <a href="https://github.com/markurtz/rustarium/discussions">Discussions</a>
</p>

______________________________________________________________________

## Overview

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/markurtz/rustarium/main/docs/assets/branding/user-flow-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/markurtz/rustarium/main/docs/assets/branding/user-flow-light.svg">
    <img alt="User Flow Diagram" src="https://raw.githubusercontent.com/markurtz/rustarium/main/docs/assets/branding/user-flow-light.svg" width="800">
  </picture>
</p>

Welcome to the rustarium repository!

### Why Use rustarium?

Coming soon!

### Comparisons

Coming soon!

## What's New

**Welcome to the rustarium Launch!**

This project has just been instantiated from the template repository. Keep an eye on this section for future release highlights, new features, and community announcements!

<!-- Once your project is active, replace the launch message above with links to your latest release notes or top 3 new features here. -->

## Quick Start

Coming soon!

## Core Concepts

This project is built using modern Python tooling, enforcing strict code quality standards with Ruff and Mypy, and providing a robust Pydantic-driven settings architecture for configuration resolution.

### Component Architecture

The repository is structured to separate documentation, application logic, and testing cleanly:

- `src/rustarium/`: The primary application source code.
- `tests/`: Comprehensive test suite ensuring reliability, organized into `unit/`, `integration/`, and `e2e/`.
- `docs/`: Source code for the MkDocs Material documentation site, including step-by-step guides, references, and getting started tutorials.
- `examples/`: Runnable reference projects demonstrating real-world configurations.
- `.github/workflows/`: Advanced CI/CD pipelines governing the project lifecycle, built around reusable workflow templates.

## Advanced Usage

Please check the [`examples/`](https://github.com/markurtz/rustarium/tree/main/examples/) directory for advanced examples and configurations.

## General

### Contributing

We welcome contributions! Please see our [Contributing Guide](https://github.com/markurtz/rustarium/blob/main/CONTRIBUTING.md) for more details. For development setup, check out [DEVELOPING.md](https://github.com/markurtz/rustarium/blob/main/DEVELOPING.md).
Please ensure you follow our [Code of Conduct](https://github.com/markurtz/rustarium/blob/main/CODE_OF_CONDUCT.md) in all interactions.

### Support and Security

- For help and general questions, see [SUPPORT.md](https://github.com/markurtz/rustarium/blob/main/SUPPORT.md).
- To report a security vulnerability, please refer to our [Security Policy](https://github.com/markurtz/rustarium/blob/main/SECURITY.md).

### AI & LLM Tooling

This repository includes first-class support for agentic and LLM-assisted development workflows:

- **[AGENTS.md](https://github.com/markurtz/rustarium/blob/main/AGENTS.md):** Repository-specific instructions for AI coding agents (Codex, Copilot Workspace, Gemini, Claude, Cursor, and similar tools). Contains the authoritative guide for project structure, executable commands, code style, and critical constraints.
- **[llms.txt](https://github.com/markurtz/rustarium/blob/main/llms.txt):** A machine-readable index of the project's documentation, following the [llms.txt specification](https://llmstxt.org/). Served at `/llms.txt` on the documentation site to help LLMs quickly locate and consume relevant content.

### License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/markurtz/rustarium/blob/main/LICENSE) file for details.

### Citations

If you use this repository or the resulting software in your research, please cite it using the following BibTeX entry:

```bibtex
@software{rustarium,
  author = {markurtz},
  title = {rustarium},
  year = 2026,
  url = {https://github.com/markurtz/rustarium}
}
```
