import torch
import torch.nn as nn

from torch.utils.data import DataLoader

@torch.no_grad()
def evaluate(model: nn.Module, data_loader: DataLoader, loss_fn):
    model.eval()
    total_error = 0
    for i, (x, y) in enumerate(data_loader):
        output = model(x)
        loss = loss_fn(output, y)
        total_error += loss
        
    return total_error/(i + 1)