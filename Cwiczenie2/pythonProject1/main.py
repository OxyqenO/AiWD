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

#zadanie 4
a4 = np.array([-10,20,-30])
b4 = np.array([1,2,3])
np.transpose(b4)
print(a4*b4)

#zadanie 5
a5 = np.array([1,2,3,4,5,6]).reshape(2,3)
asin = np.sin(a5)
print(asin)

#zadanie 6
a6 = np.array([1,2,3,4,5,6]).reshape(2,3)
acos = np.cos(a6)
print(acos)

#zadanie 7
def dodanie(a,b):
    return (a+b)
print(dodanie(a5,a6))

#zadanie 8
a8 = np.arange(9).reshape(3,3)
for i in np.nditer(a8):
    print(a8.item(i))

#zadanie 9
a9 = np.arange(9).reshape(3,3)
print(np.ndarray.flatten(a9))
flat = np.ndarray.flatten(a9)
for i in np.nditer(flat):
    print(flat[i])

#zadanie 10
a9 = np.arange(81).reshape(9,9)
print(a9)
print(a9.reshape(3,27))
print(a9.reshape(1,81))

#zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć
# ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6.
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
a11 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a11.reshape(3,4))
print(np.ndarray.flatten(a11))
print(a11.reshape(4,3))
print(np.ndarray.flatten(a11))
print(a11.reshape(2,6))
print(np.ndarray.flatten(a11))







