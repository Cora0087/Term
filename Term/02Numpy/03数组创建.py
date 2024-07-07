import numpy as np

num = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(num.shape)

a = np.zeros((3, 5))
print(a)

b = np.full(shape=(2, 3, 2), fill_value=100)
print(b)