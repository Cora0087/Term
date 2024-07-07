import time
import numpy as np
a = []
for x in range(1000000):
    a.append(x)
t1 = time.time()
sum1 = sum(a)
t2 = time.time()
print(t2-t1)

b = np.array(a)
t3 = time.time()
sum2 = np.sum(b)
t4 = time.time()
print(t4 - t3)
