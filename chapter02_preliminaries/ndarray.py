import torch

x = torch.arange(12, dtype=torch.float32)

print(x)

# number of elements in tensor
print(x.numel())

# tensor's shape
print(x.shape)

# reshape tensor from [1, 12] to [3, 4]
X = x.reshape(3, 4)
print(X)

#reshape without giving both row and  column
Y = X.reshape(4, -1)
print(Y)

#Zero
Z = torch.zeros((2, 3, 4))
print(Z)

#One
O = torch.ones((2, 3, 4))
print(O)

#Rand
R = torch.randn(3, 4)
print(R)


py_lst = torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(py_lst)
