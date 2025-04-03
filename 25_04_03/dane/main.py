import numpy as np
import pandas as pd
from pandas import DataFrame

#zadanie 1
r = np.random.randint(100, size=(30, 5)) #stwórz randomowe dane 0-100 w 5 kolumnach po 30 wierszy

punktacja = pd.DataFrame(data=r, columns=['Matematyka','Chemia','Fizyka','Biologia','Informatyka']) #stwórz dataframe na tych danych
#print(punktacja)

punktacja['Srednia'] = punktacja.mean(axis=1) #dodaj średnią jako nową kolumnę
#print(punktacja)

punktacja.to_excel("oceny.xlsx", index=False) #zapisz dataframe do pliku excel

#zadanie 2
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack'],
    'Punktacja [%]': [85, 90, 78, np.nan, 88, 76, 92, np.nan, 80, 84],
    'Frekwencja [%]': [95, 85, np.nan, 75, 88, 92, 89, 80, np.nan, 91],
    'Zaj_dodatkowe': [True, True, False, True, False, False, False, True, False, False]
}

#a) Na podstawie słownika data, stwórz DataFrame df. Kolumny utworzonego DataFrame'a nazwij kluczami słownika data.
df = pd.DataFrame(data=data)
print(df)

#b) Dodaj informacje o nowym studencie: ['Maria', 93.0, 75.0, True]
df.insert(5,['Maria', 93.0, 75.0, True], axis=1)

print(df)

#c) W danych jest błąd, student Frank chodzi na zajęcia dodatkowe. Popraw wartość w kolumnie "Zaj_dodatkowe" z False na True.
#d) W zbiorze znajdują się puste wartości. Za pomocą modułu pandas, w ich miejsce wstaw wartość 100. Wyświetl rekordy przed i po modyfikacji.
#e) Zmodyfikowane dane zapisz do pliku: new_data.csv. Podczas zapisywania pomiń indeks.

#f) Wyświetl rekordy (wiersze), gdzie Punktacja jest większa niż 85%
#g) Wyświetl średnią frekwencję wszystkich studentów. Wynik zaokrąglij do 2 miejsc po przecinku.
#h) Wyświetl wartości posortowane najpierw po Punktacji malejąco (desc), a następnie po Frekwencji rosnąco (asc)
#i) Wyświetl medianę frekwencji dla osób, które chodzą i które nie chodzą na zajęcia dodatkowe

#j) Stwórz wykres liniowy przedstawiający punktację studentów po normalizacji wartości punktacji, czyli po przeskalowaniu punktacji w zakresie 0-1, zgodnie ze wzorem:
#wzór w plikach
# Do normalizacji użyj modułu funkcji min() i max() z modułu numpy. Do wykresu dodaj siatkę, tytuł, ustaw widoczne etykiety osi x.