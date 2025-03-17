import torch

def function03(x: torch.Tensor, y: torch.Tensor):
    shape = x.shape[1]
    w = torch.rand(shape, dtype=torch.float32, requires_grad=True)
    
    n_steps = 200
    step_size = 1e-2
    
    for i in range(n_steps):
        y_pred = torch.matmul(x, w)
        mse = torch.mean((y_pred - y) ** 2)
        
        if i < 20 or i % 10 == 0:
            print(f'MSE на шаге {i + 1} {mse.item():.5f}')
            
        mse.backward()
        
        with torch.no_grad():
            w -= w.grad * step_size
            
        w.grad.zero_()
    
    return w