import torch

x = torch.arange(12, dtype=torch.float32)

X = x.reshape(3, 4)

print(X[-1], X[1:3])

#write elements
X[1, 2] = 17
print(X)


#assign multiple value
X[:2, :]= 12
print(X)