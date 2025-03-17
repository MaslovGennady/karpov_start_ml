import torch
import torch.nn as nn

from torch.utils.data import DataLoader
from torch import optim

def train(model: nn.Module, data_loader: DataLoader, optimizer, loss_fn):
    model.train()
    total_error = 0
    for i, (x, y) in enumerate(data_loader):
    
        optimizer.zero_grad()
    
        output = model(x)
    
        loss = loss_fn(output, y)
        
        total_error += loss.item()
        print(f'{loss.item():.5f}')
    
        loss.backward()
    
        optimizer.step()
        
    return total_error/(i + 1)