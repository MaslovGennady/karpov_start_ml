import torch
from torch import nn

def function04(x: torch.Tensor, y: torch.Tensor):
    n_features = x.shape[1]
    layer = nn.Linear(in_features=n_features, out_features=1)
    
    n_steps = 200
    step_size = 1e-2
    
    for i in range(n_steps):
        y_pred = layer(x).ravel()
    
        mse = torch.mean((y_pred - y) ** 2)
        
        if i < 20 or i % 10 == 0:
            print(f'MSE на шаге {i + 1} {mse.item():.5f}')
    
        mse.backward()
    
        with torch.no_grad():
            layer.weight -= layer.weight.grad * step_size
        
        layer.zero_grad()
        
    return layer