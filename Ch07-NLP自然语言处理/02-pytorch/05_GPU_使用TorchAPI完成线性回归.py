import torch
from torch import nn
from torch import optim
from matplotlib import pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 1. 定义数据
x = torch.rand([50, 1])
y = x * 3 + 0.8


# 2. 定义模型
class Lr(nn.Module):
    def __init__(self):
        super(Lr, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        out = self.linear(x)
        return out


model = Lr().to(device)
x, y = x.to(device), y.to(device)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=1e-3)

# 3. 训练模型
for i in range(30000):
    out = model(x)
    loss = criterion(y, out)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (i + 1) % 20 == 0:
        print("Epoch[{}/{}] loss={:.6f}".format(i, 30000, loss.data))


# 4. 模型评估
model.eval()
predict = model(x)
# predict = predict.data.numpy()
predict = predict.cpu().detach().numpy()
plt.scatter(x.cpu().data.numpy(), y.cpu().data.numpy(), c="r")
plt.plot(x.cpu().data.numpy(), predict)
plt.show()
