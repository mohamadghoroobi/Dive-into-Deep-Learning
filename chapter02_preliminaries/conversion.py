import numpy as np
import torch

x = torch.arange(12, dtype=torch.float32)
A = x.numpy()
B = torch.from_numpy(A)
print(type(A), type(B))

a = torch.tensor([3.5])
print(a,
      a.item(),
      float(a), 
      int(a)
      )