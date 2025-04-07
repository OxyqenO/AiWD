import random

import numpy as np

#zadanie 1
a = np.array([1,2,3])
b = np.array([1,2,3])
np.transpose(b)

print(a*b)

#zadanie 2
a2 = np.random.randint(10, 51,(3,3))
b2 = np.random.randint(10, 51,(4,4))

print(np.min(a2, axis=0))
print(np.min(a2, axis=1))

print(np.min(b2, axis=0))
print(np.min(b2, axis=1))

#zadanie 3
print (15 * a)
print (10 * b)