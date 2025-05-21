import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.cm as cm
from matplotlib.pyplot import tight_layout

#PANDAS
#1. Załaduj plik CSV jako Data Frame i wyświetl jego 4 pierwsze wiersze. Pamiętaj, przy wczytaniu zbioru Pokemon.csv parametr encoding należy ustawić na wartość latin.

df = pd.read_csv('./cw10dane/Pokemon.csv', index_col=0, encoding='latin')
print(df.head())

#2. Zgrupuj dane na podstawie wartości kolumny Type 1 następnie oblicz średnią dla wartość kolumny Defense dla każdej grupy.

srednia = df.groupby('Type 1')['Defense'].mean()
print(srednia.head())


#3. Utwórz nową kolumnę o nazwie Średnia obrona wg. Typu 1, gdzie dla każdego pokemona umieścisz obliczoną wcześniej średnią wartość obrony dla typu 1 (uwzględniając typ pokemona).

df['Srednia'] = df['Type 1'].map(srednia)
print(df.head())

#4. Utwórz nową kolumnę o nazwie Ulubiony, w której umieścisz wartość „Tak”, jeśli którykolwiek z typów Pokemona (kolumna Type 1 lub Type 2) jest typem kamiennym (wartość Rock). W przeciwnym wypadku, wstaw wartość „Nie”.

df['Ulubiony'] = df.apply(lambda x: 'Tak' if x['Type 1'] == 'Rock' or x['Type 2'] == 'Rock' else 'Nie', axis=1)
print(df.head())

#5. Utwórz nową kolumnę o nazwie Dwa typy, gdzie połączysz myślnikiem wartości z kolumny Type 1 oraz Type 2.

df['Dwa typy'] = df['Type 1'] + '-' + df['Type 2']
print(df.head())
#6. Wyświetl liczbę wierszy w zbiorze danych. Usuń ze zbioru wszystkie legendarne pokemony i ponownie wyświetl liczbę wierszy w zbiorze danych.

liczba = df['Type 1'].count()
print(liczba)

df = df[df['Legendary'] == False]
liczba = df['Type 1'].count()
print(liczba)

#7. Wyświetl liczbę wszystkich pokemonów, które nie mają drugiego typu.
df3 = df[df['Type 2'].isna()]
rows = len(df3.index)
print(rows)

#8. Zapisz zmodyfikowany Data Frame do nowego pliku modified_pokemon.csv.
df3.to_csv('modified_pokemon.csv')

#WYKRESY
#1. Na jednym płótnie (figure) wyświetl 4 różne wykresy (w dwóch rzędach i dwóch kolumnach). Ustaw wielkość płótna na (14,10).
plt.figure(figsize=(14,10))

#2. Nadaj tytuł płótna – „Analiza statystyk pokemonów regionu Kanto”. Powiększ czcionkę tytułu, dla lepszej czytelności.
plt.suptitle('Analiza statystyk pokemonów regionu Kanto', fontsize=20)
plt.subplot(2,2,1)

#3. Stwórz wykres słupkowy pokazujący średnie wartości ataku i obrony (kolumny Attack i Defense). Ustaw wybrane przez siebie kolory dla obu słupków.
x = df[['Attack', 'Defense']].mean()
plt.bar(x.index, x.values, color=['red', 'blue'])

plt.subplot(2,2,2)

#4. twórz wykres kołowy przedstawiający procentowy rozkład pokemonów w zależności od ich podstawowego typu (kolumna Type 1). Wyświetl legendę opisującą typy pokemonów i przesuń ją poza obszar wykresu. Przedstaw wartości procentowe na wykresie (użyj parametru autopct do ustawienia wartości procentowych oraz pctdistance do ustawienia ich pozycji). Upewnij się, że każdy typ ma inny kolor na wykresie.

df2 = df.groupby('Type 1')['Type 1'].count()

plt.pie(df2, autopct='%1.1f%%',pctdistance=0.7 ,labels=df2.index)

plt.legend(df2.index, loc='upper left', bbox_to_anchor=(1.15, 1))

#SEABORN
#5. Wykres punktowy zależności Sp. Def od Sp. Atk dla trzech typów Type 1 pokemonów: Dragon, Normal, Fire. Ustaw kolory dla każdego typu oraz wyświetl legendę.

plt.subplot(2,2,3)

df4 = df[df['Type 1'].isin(['Dragon', 'Normal', 'Fire'])]

x1 = df4['Sp. Def']
x2 = df4['Sp. Atk']
sns.scatterplot(data= df4, x = x1, y = x2, hue='Type 1')

#6. Boxplot przedstawiający rozkład prędkości pokemona Speed dla typu Dragon, Normal i Fire. Ustaw kolory tak jak w poprzednim podpunkcie.

plt.subplot(2,2,4)
color = ['Red', 'Green', 'Blue']
sns.boxplot(data= df4, x='Type 1', y='Speed',palette='bright', hue='Type 1')

#7. Dla zwiększenia czytelności wykresów, do każdego dodaj opisy osi oraz tytuły wykresów.

plt.subplot(2,2,1)
plt.ylabel('Wartosc')
plt.title('Atak i Obrona pokemonow')

plt.subplot(2,2,2)
plt.title('Procentowe określenie typów pokemonów')

plt.subplot(2,2,3)
plt.xlabel('Special Obrona')
plt.ylabel('Special Atak')
plt.title('Special atak względem Special obrony')

plt.subplot(2,2,4)
plt.xlabel('Typy pokemonów')
plt.ylabel('Wartość')
plt.title('Mediana prędkości dla 3 typów pokemonów')

#8. Zapisz wykres do pliku .png.
plt.tight_layout()
plt.savefig('./WykresZadanie.png')
plt.show()
