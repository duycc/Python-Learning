TRAIN_BATCH_SIZE = 512
TEST_BATCH_SIZE = 1024

TEXT_MAX_LEN = 50

import pickle

w2s = pickle.load(open("data/vocab.pkl", "rb"))
