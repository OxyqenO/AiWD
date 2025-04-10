import numpy as np

# Zadanie 1
# Za pomocą funkcji arange stwórz tablicę Numpy składającą się 20 kolejnych wielokrotności liczby 2.
tablica = np.arange(0, 41, 2)
print(tablica)


# Zadanie 2
# Stwórz listę składającą się z wartości zmiennoprzecinkowych i przypisz ją do zmiennej.
# Następnie zapisz do innej zmiennej jej kopię w postaci tablicy ndarray przekonwertowaną na typ int64.
a2 = np.arange(0.0,21.0)
b2 = np.array(list(a2), dtype='int64')

# Wyświetl listę przed konwersją i nowoutworzoną tablicę oraz zwróć uwagę na to co dzieje się z wartościami po przecinku.
print(a2)
print(b2)

# Zadanie 3
# Napisz funkcję, która będzie:
# przyjmowała jeden parametr n w postaci liczby całkowitej
# zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1
def funkcja(n):
    return np.arange(1, n*n+1, 1).reshape(n,n)
# Liczba n ma być podawana przez użytkownika. Wyświetl tablicę oraz rozmiar utworzonej tablicy.
print(funkcja(3))

# Zadanie 4
# Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji
# potęgowania oraz ilość kolejnych potęg do wygenerowania.
# Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby,
# np. generuj(2,4) -> [2 4 8 16]
def funkcja2(n,m):
    return np.int64(np.logspace(1, m, num=m, base=n))
print(funkcja2(2, 10))

# Zadanie 5
# Napisz funkcję, która:

# na wejściu przyjmuje jeden parametr określający długość wektora,
# na podstawie parametru generuje wektor, ale w kolejności odwróconej (czyli np. dla n=3 =>[3 2 1])
# generuje macierz diagonalną z w/w wektorem jako przekątną

def wektor(n):
    a = np.arange(n, 0, -1)
    b = np.diag(a)
    return b
print(wektor(6))