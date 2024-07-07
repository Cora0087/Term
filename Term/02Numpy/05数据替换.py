import numpy as np
# (3, 4)
a = np.array([
    [1, 4, 2, 5],
    [5, 6, 7, 8],
    [9, 10, 12, 13]
])
# (3, 4)
c = np.array([
    [8, 7, 255, 6],
    [5, 255, 255, 255],
    [3, 5, 255, 255]
])
"""
最后得到的数组：
a = [[ 1 4 255 5]
[ 5 255 255 255]
[ 9 10 255 255]]
"""
# b = np.zero(3, 4)
# for i in range(0, 3):
#     for j in range(0, 4):
#         if c[i][j] == 255:
#             c[i][j] = b[i][j]
#         else:
#             a[i][j] = b[i][j]
# print(b)
index = c == 255
print(index)
a[index] = 255
print(a)
index = np.where(c == 255)
print(index)
a[index] = 255
print(a)