import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
import torchvision

data_path = "data/SMSSpamCollection"


class CifarDataset(Dataset):
    def __init__(self):
        lines = open(data_path, "r")
        lines = [[l[:4].strip(), l[4:].strip()] for l in lines]
        self.df = pd.DataFrame(lines, columns=["label", "sms"])

    def __getitem__(self, index):
        single_item = self.df.iloc[index, :]
        return single_item.values[0], single_item.values[1]

    def __len__(self):
        return self.df.shape[0]


# d = CifarDataset()
# for i in range(len(d)):
#     print(i, d[i])


# dataset = CifarDataset()
# data_loader = DataLoader(dataset, batch_size=128, shuffle=True)

# for idx, (label, context) in enumerate(data_loader):
#     print(idx, label, context)
#     print("*" * 100)


dataset = torchvision.datasets.MNIST(root="./data", train=True, download=False, transform=None)
print(dataset[0])

img = dataset[0][0]
img.show()
