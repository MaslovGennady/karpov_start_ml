import torch
import torch.nn as nn
from torch.utils.data import DataLoader

@torch.inference_mode()
def predict(model: nn.Module, loader: DataLoader, device: torch.device):
    model = model.to(device)
    predictions = []
    model.eval()
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        output = model(inputs)
        _, predicted_classes = torch.max(output, dim=1)
        predictions.append(predicted_classes.cpu())
        
    return torch.cat(predictions)