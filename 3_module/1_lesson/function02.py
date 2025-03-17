import torch

def function02(tensor: torch.Tensor) -> torch.Tensor:
    shape = tensor.shape[1]
    return torch.rand(shape, dtype=torch.float32, requires_grad=True)