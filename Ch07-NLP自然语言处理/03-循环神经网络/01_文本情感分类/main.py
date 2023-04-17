from word2sequence import Word2Sequence
from dataset import get_dataloader
import pickle
from tqdm import tqdm

if __name__ == '__main__':
    w2s = Word2Sequence()
    dl_train = get_dataloader(True)
    dl_test = get_dataloader(False)
    for texts, label in tqdm(dl_train, total=len(dl_train)):
        for sentence in texts:
            w2s.fit(sentence)
    for texts, label in tqdm(dl_test, total=len(dl_test)):
        for sentence in texts:
            w2s.fit(sentence)
    w2s.build_vocab()
    pickle.dump(w2s, open("data/vocab.pkl", "wb"))
