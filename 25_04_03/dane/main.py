from operator import index

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import yscale
from pandas import DataFrame

#zadanie 1
r = np.random.randint(100, size=(30, 5)) #stwórz randomowe dane 0-100 w 5 kolumnach po 30 wierszy

punktacja = pd.DataFrame(data=r, columns=['Matematyka','Chemia','Fizyka','Biologia','Informatyka']) #stwórz dataframe na tych danych
print(punktacja, '\n')

punktacja['Srednia'] = punktacja.mean(axis=1) #dodaj średnią jako nową kolumnę
print(punktacja, '\n')

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
print(df, '\n')

#b) Dodaj informacje o nowym studencie: ['Maria', 93.0, 75.0, True]
data2 = {
    'Student': ['Maria'],
    'Punktacja [%]': [93.0],
    'Frekwencja [%]': [75.0],
    'Zaj_dodatkowe': [True]
}
df2 = pd.DataFrame(data=data2)
df = pd.concat([df, df2], ignore_index=True)
print(df, '\n')

#c) W danych jest błąd, student Frank chodzi na zajęcia dodatkowe. Popraw wartość w kolumnie "Zaj_dodatkowe" z False na True.
df.loc[5, 'Zaj_dodatkowe'] = True

print(df, '\n')

#d) W zbiorze znajdują się puste wartości. Za pomocą modułu pandas, w ich miejsce wstaw wartość 100. Wyświetl rekordy przed i po modyfikacji.
df = df.fillna(100)

print(df, '\n')

#e) Zmodyfikowane dane zapisz do pliku: new_data.csv. Podczas zapisywania pomiń indeks.
df.to_csv("new_data.cvs", index=False)

#f) Wyświetl rekordy (wiersze), gdzie Punktacja jest większa niż 85%
punktacja = df[df['Punktacja [%]']>85]
print(punktacja, '\n')

#g) Wyświetl średnią frekwencję wszystkich studentów. Wynik zaokrąglij do 2 miejsc po przecinku.
srednia = df['Frekwencja [%]'].mean().round(2)
print(srednia, '\n')

#h) Wyświetl wartości posortowane najpierw po Punktacji malejąco (desc), a następnie po Frekwencji rosnąco (asc)
sort1 = df.sort_values('Punktacja [%]', ascending=False)
print(sort1, '\n')
sort2 = df.sort_values('Frekwencja [%]', ascending=True)
print(sort2, '\n')

#i) Wyświetl medianę frekwencji dla osób, które chodzą i które nie chodzą na zajęcia dodatkoweDD
mediana_chodza = df.loc[df['Zaj_dodatkowe'] == True, 'Frekwencja [%]'].median()
mediana_nie_chodza = df.loc[df['Zaj_dodatkowe'] == False, 'Frekwencja [%]'].median()

print(mediana_chodza)
print(mediana_nie_chodza, '\n')

#j) Stwórz wykres liniowy przedstawiający punktację studentów po normalizacji wartości punktacji, czyli po przeskalowaniu punktacji w zakresie 0-1, zgodnie ze wzorem:
#wzór w plikach

plt.figure(figsize=(10, 5))
plt.plot(df['Student'], df['Punktacja [%]'], marker='o', linestyle='-', color='blue')
plt.title('Punktacja studentów')
plt.xlabel('Student')
plt.ylabel('Punktacja [%]')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Do normalizacji użyj modułu funkcji min() i max() z modułu numpy. Do wykresu dodaj siatkę, tytuł, ustaw widoczne etykiety osi x.