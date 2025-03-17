import torch
import torch.nn as nn


class Similarity2(nn.Module):
    def __init__(self, encoder_dim: int, decoder_dim: int, intermediate_dim: int):
        super().__init__()

        self.fc1 = nn.Linear(encoder_dim, intermediate_dim)
        self.fc2 = nn.Linear(decoder_dim, intermediate_dim)
        self.fc3 = nn.Linear(intermediate_dim, 1)
        self.tanh = nn.Tanh()

    def forward(self, encoder_states: torch.Tensor, decoder_state: torch.Tensor):
        # encoder_states.shape = [T, N]
        # decoder_state.shape = [N]

        # Применяем fc1 к каждому состоянию энкодера
        encoder_transformed = self.fc1(encoder_states)  # [T, intermediate_dim]
        
        # Применяем fc2 к состоянию декодера
        decoder_transformed = self.fc2(decoder_state)    # [intermediate_dim]

        # Теперь добавляем результаты (broadcasting)
        combined = encoder_transformed + decoder_transformed  # [T, intermediate_dim]

        # Применяем tanh
        combined_tanh = self.tanh(combined)  # [T, intermediate_dim]

        # Применяем fc3 для получения сходства
        similarity_scores = self.fc3(combined_tanh)  # [T, 1]

        return similarity_scores  # Возвращаем вектор сходства [T]