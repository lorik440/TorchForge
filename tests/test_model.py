import torch
from torch import nn

from torchfoundry.model import createModel

# test loadModel loads a single layer nn
layers=(
    nn.Linear(2,1)
)
def test_load_model_runs_layers():
    model = createModel(layers)
    model_device = next(model.parameters()).device

    output = model(torch.ones((2),device=model_device))

    assert output.shape ==torch.Size([1])
