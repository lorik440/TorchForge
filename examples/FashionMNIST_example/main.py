import torchfoundry as tf
from torchfoundry import torch
from torchfoundry import nn
from torchvision.transforms import ToTensor

train_data, test_data=tf.loadDataset(
    "FashionMNIST", 
    shuffle=True, 
    root="examples/FashionMNIST_example/data",
    transformer=ToTensor())

layers=(
    nn.Flatten(),
    nn.Linear(28*28,64),
    nn.ReLU(),
    nn.Linear(64,16),
    nn.ReLU(),
    nn.Linear(16,10)
)

model =tf.createModel(
    layers, 
    path="examples/FashionMNIST_example/model.pth", 
    Summary=True, 
    input_size=(1,1,28,28)
)

optimizer =torch.optim.Adam(model.parameters(),lr=0.0001)
loss_fn=nn.CrossEntropyLoss()

model= tf.trainModel(
    model,
    train_data,
    loss_fn, 
    optimizer, 
    epoch=5)

tf.saveModel(model, path="examples/FashionMNIST_example/model.pth")



