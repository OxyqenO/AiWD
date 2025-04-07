from array import array

import numpy as np

#zadanie 1
a1 = np.arange(0, 41, 2)

print(a1)

#zadanie 2

a2 = np.arange(0.0,10.0)
b2 = np.array(list(a2), dtype='int64')
print(b2.dtype)
print(a2)

#zadanie 3

def generuj_tablice(n):
    return print(np.arange(1, n*n + 1).reshape(n, n))

n = 10
generuj_tablice(n)

#zadanie 4

def generuj(n,m):
    return print(np.int64(np.logspace(1, m, num=m, base=n)))
generuj(2,4)

#zadanie 5
def wektor(n):
    a = np.arange(n,0,-1)
    b = np.diag(a)
    return print(b)
wektor(5)

#zadanie 6

#zadanie 7
def funkcja(n):
    a = np.zeros([n, n])
    np.fill_diagonal(a, 2)
    for i in range(1, n):
        a += np.diag(np.full(n - i, 2 * (i + 1)), i)
        a += np.diag(np.full(n - i, 2 * (i + 1)), -i)
    return print(a)
funkcja(4)

#zadanie 8

def podziel_tablice(tablica, kierunek='poziom'):
    if kierunek == 'poziom':
        if tablica.shape[1] % 2 != 0:
            print("Nie można podzielić tablicy w poziomie – liczba kolumn jest nieparzysta.")
            return
        polowa = tablica.shape[1] // 2
        lewa, prawa = np.hsplit(tablica, 2)
        print("Lewa część:")
        print(lewa)
        print("Prawa część:")
        print(prawa)

    elif kierunek == 'pion':
        if tablica.shape[0] % 2 != 0:
            print("Nie można podzielić tablicy w pionie – liczba wierszy jest nieparzysta.")
            return
        polowa = tablica.shape[0] // 2
        gora, dol = np.vsplit(tablica, 2)
        print("Górna część:")
        print(gora)
        print("Dolna część:")
        print(dol)
    else:
        print("Nieznany kierunek. Użyj 'poziom' lub 'pion'.")

# Przykład użycia:
tablica = np.arange(16).reshape(4, 4)
podziel_tablice(tablica, kierunek='pion')






