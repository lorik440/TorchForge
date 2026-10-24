from pathlib import Path
from typing import Literal

import torch
from rich import print
from torch import nn
from torchinfo import summary

Summary=Literal[True,False]
def loadModel(layers,load_dict=None,Summary: bool=False, input_size=None):
    """
       Creates a PyTorch neural network and optionally loads pretrained weights
    and displays a model summary.

    Args:
        layers (list[nn.Module]): PyTorch layers used to construct the model.
        path (str | None): Path to a saved model state dictionary.
        Summary (bool): Whether to display the model summary.
        input_size (tuple | None): Dimensions of the model input, excluding
            the batch dimension. Required if Summary is True.

    Returns:
        nn.Module: The constructed neural network.

    Raises:
        ValueError: If the path or input_size is invalid.
        FileNotFoundError: If the checkpoint file does not exist.
    """

    #model device runtime 
    if torch.accelerator.is_available():
        device=torch.accelerator.current_accelerator
    else:
        device='cpu'

    class NeuralNetwork(nn.Module):
        def __init__(self):
            super().__init__()

            self.layers=nn.Sequential(*layers)

        def forward(self,x):
            x=self.layers(x)
            return x

    model =NeuralNetwork().to(device)

    #loading model
    if load_dict is not None:

        if not isinstance(load_dict, str):
            raise ValueError("[red]path parameter must be string[/red]")
        model_path= Path(load_dict)

        if model_path.exists():
            print("loading model..." ,flush=True)
            model.load_state_dict(
                torch.load(
                    model_path,
                    map_location=device,
                    weights_only=True
                )
            )

            print("model created")
        else:
            print("[red]model path not found[/red]. Starting fresh")

    #printing the model summary
    if Summary:
        if input_size is None:
            raise ValueError("input_size canot be None when Summary is True")
        summary(
            model,
            input_size=input_size,
            col_names=["input_size","output_size","num_params","trainable"],
            depth=1
        )
    
    return model

def  saveModel(model,path):
    if not model:
        raise ValueError("model is a required parameter")
    if not path:
        raise ValueError("path is a required parameter")
    if not isinstance(path, (str,Path)):
        raise ValueError("path must be string or pathlib.Path")
    if not isinstance(model, nn.Module):
        raise ValueError("module must be a Pytorch nn.Module")

    torch.save(model.state_dict(),path)
    print(f"model saved at: {path} ")
