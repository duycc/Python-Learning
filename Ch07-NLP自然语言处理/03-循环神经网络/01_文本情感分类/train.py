import config
from model import ImdbModel
from dataset import get_dataloader
from torch.optim import Adam
from tqdm import tqdm
import torch.nn.functional as F

model = ImdbModel()
optimizer = Adam(model.parameters())


def train(epoch):
    train_dataloader = get_dataloader(train=True)
    bar = tqdm(train_dataloader, total=len(train_dataloader))
    for idx, (input, target) in enumerate(bar):
        optimizer.zero_grad()
        output = model(input)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        bar.set_description("epcoh:{}  idx:{}   loss:{:.6f}".format(epoch, idx, loss.item()))


if __name__ == '__main__':
    for i in range(10):
        train(i)
