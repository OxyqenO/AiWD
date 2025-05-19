import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#zad 1
#Stwórz i wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. Opisz linię wykresu dodając legendę z
# etykietą f(x) = 1/x. Dodaj odpowiednie etykiety do obu osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na
# (0, 1) oraz (0, długość wektora x).

#x = np.linspace(1,20)
#f = 1/x
#plt.plot(f)
#plt.axis(xmax=20)
#plt.title("Wykres funkcji")
#plt.legend(['f(x) = 1/x'])
#plt.xlabel("x")
#plt.ylabel("f(x)")
#plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 2
#Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak poniżej.

#plt.plot(f, marker='>', color='green', linestyle='dotted', label='f(x) = 1/x')
#plt.axis(xmax=20)
#plt.xlabel("x")
#plt.ylabel("f(x)")
#plt.legend()
#plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 3 + zad 4
#Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. Dodaj etykiety
#i legendę do wykresu.

#Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji, tak aby osiągnąć efekt podobny
#do tego na poniższym zrzucie ekranu.

# x = np.arange(0,30,0.1)
# sin = np.sin(x)
# sin2 = np.sin(-x)
# cos = np.cos(x)
# plt.plot(x,sin + 2,label='sin(x)')
# #plt.plot(x,cos,label='cos(x)')
# plt.plot(x,sin2,label='sin(x)')
# #plt.legend(['sin(x)','cos(x)'], loc='upper right')
# plt.legend(['sin(x)','sin(x)'], loc='upper right')
# plt.ylabel('sin(x)')
# plt.xlabel('x')
# plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 5
#Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris)
#wygeneruj wykres punktowy, gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’,
#dodaj paletę kolorów c (na przykładzie kodu z podpunktu 2. Wykres punktowy), a parametr s niech
#będzie wartością bezwzględną z różnicy wartości poszczególnych elementów wektorów x oraz y.

# data = pd.read_csv('iris.data', sep=',')
# print(data)
#
# x = data['sepal length']
# y = data['sepal width']
#
# plt.scatter(x, y, s=(x-y)*7.5, c=(np.random.randint(0, 150, 150)))
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 6
#Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci (imiona.xlsx).
#Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety.
#Poustawiaj różne kolory dla wykresów.
#1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym datasecie.
#2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla
#każdego roku z osobna. Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
#3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.

# df=pd.read_excel('dane/imiona.xlsx')
#
# plt.subplot(1,3,1)
# plt.bar(df['Plec'].unique(),df.groupby('Plec')['Liczba'].sum())
#
# plt.subplot(1,3,2)
# dates=df['Rok'].unique()
# yby=[df[df['Plec']=='K'].groupby(['Rok'])['Liczba'].sum(),
#      df[df['Plec']=='M'].groupby(['Rok'])['Liczba'].sum()]
# plt.plot(dates,yby[0])
# plt.plot(dates,yby[1])
#
# plt.subplot(1,3,3)
# plt.bar(dates,df.groupby(['Rok'])['Liczba'].sum())
#
# plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 7
#Napisz funkcję, która losowo rzuca dwiema kostkami d6 n razy. Wynik rzutów zapisywany jest w postaci
#listy sum oczek z tych dwóch kostek. Np. rzucaj(6) generuje 6 rzutów kostkami i zwraca wektor 6 sum
# oczek każdego rzutu. Po zakończeniu funkcji wyświetlaj histogram sumy rzutów. Dodaj stosowne etykiety
#do wykresu.

# def kosci(n):
#     lista = []
#     for i in range(n):
#         lista.append(np.random.randint(1,7) + np.random.randint(1,7))
#     return lista
# data = kosci(1000)
# plt.ylabel('Ilość rzutów')
# plt.xlabel('Ilość oczek')
# plt.hist(data, edgecolor='b')
# plt.xticks(np.arange(min(data), max(data)+1, 1.0))
# plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 8
#Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień dla każdego sprzedawcy i wyświetl
#wykres kołowy z procentowym udziałem każdego sprzedawcy w ogólnej sumie zamówień.

df = pd.read_csv('zamowienia.csv', sep=';')
print(df.head())
x = df.groupby('Sprzedawca')['idZamowienia'].count()
print(x.head())
plt.pie(x, autopct='%1.1f%%', labels=x.index)
plt.show()