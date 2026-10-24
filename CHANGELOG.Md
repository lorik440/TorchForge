# Changelog

Notable changes to TorchFoundry are documented in this file. Each version includes a summary of the changes made, including new features, bug fixes, and other improvements.

## [Unreleased]

### Added
- Initial dataset, model, and training utility module scaffolding.
- GitHub Actions checks for Ruff, pytest, and distribution builds.

### Changed
- Renamed the project and Python package from TorchForge to TorchFoundry.
- Added package metadata, runtime dependencies, and development dependencies.
- Readme file updated to reflect the new project name and provide installation instructions.

### Removed
- Removed the TensorBoard requirement.

### Fixed
- Fixed the `model.py` file to include the correct package name and metadata.
- Fixed the `loadModel()` for better model architectyre loading and initialization.
- Fixed the `` to include the correct package name and metadata.
- Fixed `test_load_model_runs_layers()` match the expected model architecture and layer count.


