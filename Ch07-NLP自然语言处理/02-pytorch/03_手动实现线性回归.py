import torch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x = torch.rand([50])
y = 3 * x + 0.8

w = torch.rand(1, requires_grad=True)
b = torch.rand(1, requires_grad=True)


def loss_fn(y, y_predict):
    loss = (y_predict - y).pow(2).mean()
    # for i in [w, b]:
    #     if i.grad is not None:
    #         i.grad.data.zero_()
    [i.grad.data.zero_() for i in [w, b] if i.grad is not None]
    loss.backward()
    return loss.data


def optimize(learning_rate):
    w.data -= learning_rate * w.grad.data
    b.data -= learning_rate * b.grad.data


def main():
    for i in range(3000):
        y_predict = x * w + b
        loss = loss_fn(y, y_predict)

        if i % 500 == 0:
            print("i={} w={} b={} loss={}".format(i, w.item(), b.item(), loss.data))
        optimize(0.01)

    predict = x * w + b
    plt.scatter(x.data.numpy(), y.data.numpy(), c="r")
    plt.plot(x.data.numpy(), predict.data.numpy())
    plt.show()


if __name__ == "__main__":
    main()
