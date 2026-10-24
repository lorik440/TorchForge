import torch
from torch import nn

from torchfoundry.model import loadModel


def test_load_model_runs_layers():
    model = loadModel([nn.Linear(2, 1)])
    model_device = next(model.parameters()).device

    output = model(torch.ones((1, 2), device=model_device))

    assert output.shape == (1, 1)
