import torch
import torch.nn as nn


class Similarity1(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, encoder_states: torch.Tensor, decoder_state: torch.Tensor):
        # encoder_states.shape = [T, N]
        # decoder_state.shape = [N]
        
        # Вычисляем скалярное произведение между состоянием декодера и состояниями энкодера
        # encoder_states.T имеет форму [N, T], а decoder_state имеет форму [N]
        similarity_scores = torch.matmul(encoder_states, decoder_state)  # [T, N] @ [N] -> [T]
        
        return similarity_scores