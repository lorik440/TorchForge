import torch
from torch import nn
from torch.utils.data import DataLoader


def trainModel(model, dataloader, loss_fn, optimizer, epoch, save_dict=None ):

    if not isinstance(model, nn.Module):
        raise TypeError("module must be a Pytorch nn.Module")
    if not isinstance(dataloader,DataLoader):
        raise TypeError(
            "dataloader must be an instance of torch.utils.data.DataLoader"
        )
    if not isinstance(epoch,int):
        raise ValueError("epoch must be integer")
    if not isinstance(save_dict, str):
        raise ValueError("save_dict must be string")

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
                
    if save_dict is not None:
        try:
            torch.save(model.state_dict(), save_dict)
            print(f"model was saved at '{save_dict}'")
        except (OSError, RuntimeError) as e:
            raise RuntimeError(f"Failed to save model state_dict: {e}") from e


