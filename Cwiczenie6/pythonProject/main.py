from operator import index

import numpy as np
import pandas as pd
from pandas import DataFrame


#zadanie 1
# a) Utwórz pandas.DataFrame wypełniony losowymi liczbami całkowitymi z zakresu 0-100 (rozmiar: 5 kolumn, 30 wierszy). Liczby wygeneruj przy użyciu numpy.
a1 = np.random.randint(0,101,(3,5))
df1 = DataFrame(data=a1)
print(df1, '\n')

# b) Nadaj kolumnom nazwy odpowiadające przedmiotom szkolnym: [Matematyka, Chemia, Fizyka, Biologia, Informatyka]
df1.rename(columns={0:'Matematyka', 1:'Chemia', 2:'Fizyka', 3:'Biologia', 4:'Informatyka'}, inplace=True)
print(df1, '\n')

# c) Dodaj kolumnę Średnia, która przechowuje średnią ucznia ze zdobytych punktacji z każdego z przedmiotów.
df1.loc[:,'Srednia'] = np.mean(df1, axis=1)
print(df1, '\n')

# d) Zapisz nowoutworzony zbiór danych do pliku oceny.xlsx. Podczas zapisywania pomiń indeks.
df1.to_excel("oceny.xlsx", index=False)



#zadanie 2
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack'],
    'Punktacja [%]': [85, 90, 78, np.nan, 88, 76, 92, np.nan, 80, 84],
    'Frekwencja [%]': [95, 85, np.nan, 75, 88, 92, 89, 80, np.nan, 91],
    'Zaj_dodatkowe': [True, True, False, True, False, False, False, True, False, False]
}

# a) Na podstawie słownika data, stwórz DataFrame df. Kolumny utworzonego DataFrame'a nazwij kluczami słownika data.
df = DataFrame(data=data)
print(df, '\n')

# b) Dodaj informacje o nowym studencie: ['Maria', 93.0, 75.0, True]
df.loc[10] = ['Maria', 93.0, 75.0, True]
print(df, '\n')

# c) W danych jest błąd, student Frank chodzi na zajęcia dodatkowe. Popraw wartość w kolumnie "Zaj_dodatkowe" z False na True.
df.loc[5] = ['Frank', 76.0, 92.0, True]
print(df, '\n')

# d) W zbiorze znajdują się puste wartości. Za pomocą modułu pandas, w ich miejsce wstaw wartość 100. Wyświetl rekordy przed i po modyfikacji.
print('przed: ', df)
df.loc[np.isnan(df['Punktacja [%]']), 'Punktacja [%]'] = 100
df.loc[np.isnan(df['Frekwencja [%]']), 'Frekwencja [%]'] = 100
print('\npo: ', df, '\n')
# e) Zmodyfikowane dane zapisz do pliku: new_data.csv. Podczas zapisywania pomiń indeks.
df.to_csv('new_data.csv',index=False)