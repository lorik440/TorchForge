# TODO

## Data (`data.py`)

- [x] Finish `loadDataset` by adding dataset initialization and implementing the train/test selector paths.
- [x] Make the dataset configurable instead of hardcoding FashionMNIST (accept a dataset class or name parameter).
- [x] Fix `batch_size` validation — the docstring says 1–128 but the check `not 0 < batch_size < 128` rejects 128.
- [x] Add a `num_workers` and `shuffle` parameter so users can control DataLoader behavior.

## Model (`model.py`)

- [x] Rename `load_dict` to `path` (or vice versa) so the parameter name matches the docstring.
- [x] Rename the `Summary` parameter to `show_summary` to avoid shadowing the `Summary` type alias.
- [ ] Validate that the `layers` list is non-empty before constructing `nn.Sequential`.
- [ ] Have `saveModel` create parent directories automatically when they don't exist.
- [ ] Move the `NeuralNetwork` class to module level instead of redefining it on every `loadModel` call.

## Training (`training.py`)

- [x] Fix `trainModel` validation so its default `save_dict=None` value is accepted instead of raising `ValueError`.
- [x] Validate that `epoch` is a positive integer (> 0).
- [x] Add type and value validation for `loss_fn` and `optimizer`.
- [ ] Add optional learning-rate scheduler support (pass a scheduler, step it per epoch).
- [ ] Add optional validation/accuracy tracking after each epoch.
- [ ] Add an optional early-stopping mechanism based on validation loss.
- [ ] Add a progress bar (e.g. tqdm) for batch-level progress within each epoch.

## Package & Exports (`__init__.py`)

- [ ] Re-export public API (`loadModel`, `saveModel`, `loadDataset`, `trainModel`) so users can write `from torchfoundry import loadModel`.

## Testing

- [ ] Expand pytest coverage for dataset loading, model save/load behavior, and the training loop.
- [ ] Add tests for `saveModel` (round-trip save → load, invalid path, invalid model type).
- [ ] Add tests for `loadModel` edge cases (empty layers list, missing checkpoint file, summary without input_size).
- [ ] Add tests for `trainModel` input validation (invalid model, dataloader, epoch, save_dict).

## Examples & Docs

- [ ] Add example scripts in `examples/` showing end-to-end model creation, training, and saving.
- [ ] Add a CONTRIBUTING.md with setup instructions for new contributors.