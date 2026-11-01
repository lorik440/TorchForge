# Contributing to TorchFoundry

First of all, thank you for considering contributing to TorchFoundry!

TorchFoundry is an open-source Python library built to simplify everyday PyTorch workflows. Whether you're fixing a bug, improving documentation, suggesting a feature, or contributing code, your help is appreciated.

These guidelines explain how to contribute to the project.

## Getting Started

### 1. Fork the Repository

Fork the repository to your GitHub account:

https://github.com/lorik440/TorchFoundry

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/TorchFoundry.git
cd TorchFoundry
```

### 3. Set Up the Development Environment

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install the project and development dependencies:

```bash
pip install -e ".[dev]"
```

If development dependencies are not configured in `pyproject.toml`, install the required tools separately.

## What Can You Contribute?

Contributions are welcome in several areas:

* **Bug fixes:** Identify and fix issues in existing functionality.
* **New features:** Introduce useful utilities that improve PyTorch workflows.
* **Documentation:** Improve explanations, examples, and API documentation.
* **Performance:** Improve efficiency without unnecessarily increasing complexity.
* **Testing:** Add tests and improve existing test coverage.
* **Code quality:** Refactor code to improve readability and maintainability.

Before implementing a major feature, open an issue to discuss the idea first.

## Development Guidelines

To keep TorchFoundry consistent and maintainable, please follow these guidelines:

* Write clean, readable, and maintainable Python code.
* Follow PEP 8 conventions.
* Use meaningful variable, function, and class names.
* Add docstrings to public functions and classes.
* Handle errors appropriately and provide useful error messages.
* Avoid unnecessary dependencies.
* Keep implementations simple and beginner-friendly.
* Preserve compatibility with supported Python and PyTorch versions.
* Avoid introducing breaking changes without discussing them first.

## Testing

Before submitting a pull request, make sure your changes work
