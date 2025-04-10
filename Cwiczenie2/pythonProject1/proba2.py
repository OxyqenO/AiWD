import numpy as np

# Zadanie 1
# Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.
a1 = np.array([1,2,3])
print(a1)
b1 = np.array([5,6,7])
print(b1)
c1 = a1*b1
print(c1, '\n')

# Zadanie 2
# Utwórz macierz 3x3 oraz 4x4. Wypełnij je wartościami losowymi (np.random.randint()) w zakresie od <10,50>.
# Wyświetl macierze oraz znajdź najniższe wartości dla każdej kolumny i każdego rzędu.
a2 = np.random.randint(10, 51,(3,3))
b2 = np.random.randint(10, 51,(3,3))
print(a2,'\n')
print(b2,'\n')
print(np.min(a2, axis=0))
print(np.min(a2, axis=1))
print(np.min(b2, axis=0))
print(np.min(b2, axis=1))

# Zadanie 3
# Wykorzystaj macierze z zadania pierwszego i oblicz iloczyn skalarny macierzy.
print(np.mean(a1))
print(np.mean(b1))
print(np.mean(c1))

# Zadanie 4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste.
# Następnie wykonaj na nich operację mnożenia. Funkcje uniwersalne

# Zadanie 5
# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.

# Zadanie 6
# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.

# Zadanie 7
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
