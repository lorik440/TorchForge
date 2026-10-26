import torch
from torch import nn
from torch.utils.data import DataLoader
from pathlib import Path
from torchfoundry import saveModel

def trainModel(model, dataloader, loss_fn, optimizer, epoch, path=None ):
    """
    Trains a PyTorch model for the specified number of epochs and optionally
    saves its state dictionary.

    Args:
        model (nn.Module): PyTorch model to train.
        dataloader (DataLoader): DataLoader providing the training batches.
        loss_fn: Loss function used to compare predictions with targets.
        optimizer: Optimizer used to update the model parameters.
        epoch (int): Number of training epochs.
        save_dict (str | None): Path where the model state dictionary is saved.

    Returns:
        None

    Raises:
        TypeError: If model or dataloader has an invalid type.
        ValueError: If epoch or save_dict has an invalid type.
        RuntimeError: If saving the model state dictionary fails.
    """

    if not isinstance(model, nn.Module):
        raise TypeError("module must be a Pytorch nn.Module")
    if not isinstance(dataloader,DataLoader):
        raise TypeError( "dataloader must be an instance of torch.utils.data.DataLoader")
    if not isinstance(epoch,int):
        raise ValueError("epoch must be integer")
    if epoch <0:
        raise ValueError("epoch must be positive integer")


    if torch.accelerator.is_available():
        device=torch.accelerator.current_accelerator
    else:
        device="cpu"
    
    size=len(dataloader.dataset)

    model.train()
    for e in range(epoch):
        print("")
        print(f"epoch:{e+1}")
        for batch, (x,y) in enumerate(dataloader):
            x=x.to(device)
            y=y.to(device)

            pred=model(x)
            loss=loss_fn(pred,y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if batch % 100==0:
                loss=loss.item()
                current=(batch+1)*len(x)

                print(f"loss: {loss:>7f} [{current:>5d}/{size:>5d}]")
                
    if path is not None:
        if not isinstance(path, (str, Path)):
            raise ValueError("save_dict must be string or pathlib.Path")
        
        saveModel(model,path)

    return model