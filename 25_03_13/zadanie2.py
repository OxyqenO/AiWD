import numpy as np

a = np.random.randint(10,51,(3,3))
b = np.random.randint(10,51,(4,4))

print("a \n", a, '\n')

print('Min column a:', np.min(a, axis=0))
print('Min row a:', np.min(a, axis=1))

print("b \n",b, "\n")

print("Min column b:", np.min(b, axis=0))
print("Min row b:", np.min(b, axis=1))