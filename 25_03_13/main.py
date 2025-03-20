import numpy as np

def przyklad1():
    b = np.arange(12).reshape(3,4)

    print(b)

    print(b.sum())

    print(b.sum(axis=0))
    print(b.sum(axis=1))

    print(b.min(axis=1))

    print(b.cumsum(axis=1))

#przyklad1()

def przyklad2():
    a = np.arange(3)
    b = np.arange(3)

    print(a.dot(b)) #iloczyn skalarny macierzy
    print(np.dot(a,b)) #inny sposób
#przyklad2()

def przyklad3():
    a = np.ones(3, dtype=np.int32)
    print(a)
    print(a.dtype.name)
    
przyklad3()