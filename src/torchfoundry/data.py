from typing import Literal

from torch.utils.data import DataLoader

Selector=Literal["train","test"]

def loadDataset(selector:Selector| None=None, batch_size: int=64):
    """
    Get a FashionMNIST DataLoader.

    Parameters
    ----------
    selector : {"train", "test"} or None, default=None
        Select which dataset to return.
        None returns both DataLoaders.

    batch_size : int, default=64
        Number of samples per batch (1-128).

    Returns
    -------
    DataLoader or tuple[training_data, testing_data]
        The selected DataLoader, or both DataLoaders.
    """
    if type(batch_size) is not int:
        raise ValueError("batch_size must be an integer")
    if not 0 < batch_size < 128:
        raise ValueError("batch_size must be between 1 and 128")

    trainData= "not finished"
    testData="not finished"
    raise ValueError("still in development")

    if selector =="train":
        training_data= DataLoader(trainData,batch_size=batch_size, shuffle=True)
        return training_data
    elif selector =="test":
        testing_data= DataLoader(testData, batch_size=batch_size, shuffle=True)
        return testing_data
    elif selector is None:
        training_data= DataLoader(trainData,batch_size=batch_size, shuffle=True) 
        testing_data= DataLoader(testData, batch_size=batch_size, shuffle=True)
        return training_data, testing_data
    else:
        raise ValueError("selector must have value { test / train / None }")

