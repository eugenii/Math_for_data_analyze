import numpy as np

c = np.array([3, -2, 8])
d = np.array([4, 10, 6])
a = 4 * c - 2.5 * d
b = -c + 3 * d

print(a)
print(b)
print(a @ b)