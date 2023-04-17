import torch.nn as nn
import config
import torch.nn.functional as F


class ImdbModel(nn.Module):
    def __init__(self):
        super(ImdbModel, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=len(config.w2s), embedding_dim=300, padding_idx=config.w2s.PAD)
        self.fc = nn.Linear(config.TEXT_MAX_LEN * 300, 2)

    def forward(self, input):
        input_embeded = self.embedding(input)
        input_embeded_viewed = input_embeded.view(input_embeded.size(0), -1)
        out = self.fc(input_embeded_viewed)
        return F.log_softmax(out, dim=-1)
