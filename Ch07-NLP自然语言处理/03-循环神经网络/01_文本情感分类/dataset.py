"""
准备数据
"""
from torch.utils.data import DataLoader, Dataset
import torch
import os
import util
import config


class ImdbDataset(Dataset):
    def __init__(self, train=True):
        super(ImdbDataset, self).__init__()
        data_base_path = "data/aclImdb/"
        data_path = os.path.join(data_base_path, "train" if train else "test")
        self.total_path = []
        for temp_path in ["pos", "neg"]:
            curr_path = os.path.join(data_path, temp_path)
            self.total_path += [os.path.join(curr_path, file) for file in os.listdir(curr_path) if file.endswith(".txt")]

    def __getitem__(self, idx):
        file = self.total_path[idx]
        tokens = util.tokenlize(open(file).read().strip())
        label = int(file.split("_")[-1].split(".")[0])
        label = 0 if label < 5 else 1
        return tokens, label

    def __len__(self):
        return len(self.total_path)


def collate_fn(batch):
    reviews, labels = zip(*batch)
    reviews = torch.LongTensor([config.w2s.transform(i, max_len=config.TEXT_MAX_LEN) for i in reviews])
    labels = torch.LongTensor(labels)
    return reviews, labels


def get_dataloader(train=True):
    dataset = ImdbDataset(train)
    batch_size = config.TRAIN_BATCH_SIZE if train else config.TEST_BATCH_SIZE
    return DataLoader(dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)


if __name__ == '__main__':
    for idx, (review, label) in enumerate(get_dataloader(train=True)):
        print(idx)
        print(review)
        print(label)
        break
