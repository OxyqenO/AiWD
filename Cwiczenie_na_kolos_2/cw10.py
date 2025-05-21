import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Ustawienie stylu wykresów (tło jasne)
sns.set_style('whitegrid')

# Załadowanie zbioru 'Pokemon.csv' do zmiennej df. Prosze zwrócić uwagę na dodatkowe argumenty
# index_col=0 - ustalenie pierwszej kolumny jako kolumna indeksująca
# encoding='latin' - załadowanie
df = pd.read_csv('./cw10dane/Pokemon.csv', index_col=0, encoding='latin')

# Tam gdzie nazwy kolumn mają spacje, zastąpimy je podkreślnikiem '_'
df.columns = [c.replace(' ', '_') for c in df.columns]

# Wypisanie 5 pierwszych rzędów zbioru wraz z nagłówkami
print(df.head())

#-----------------------------------------------------------------------------------------------------------

#Zadanie 1 - Stwórz wykres punktowy (scatter plot)

# Wykres ma przedstawiać zależność ataku (Attack) od obrony (Defense) dla pokemonów mających wyłącznie jeden
# typ (kolumna Type 2 bez wartości) dla 3 róznych etapów ewolucji pokemonów (kolumna Stage).
#
# pogrupuj elementy względem ewolucji pokemona - skorzystaj z parametru 'hue'
# aby sprawdzić czy Type 2 ma wartość NaN, wykorzystaj funkcję isnull())
# na osi x przedstaw atak, a na osi y obronę pokemona
# przesuń legendę wykorzystując funkcję sns.move_legend() https://seaborn.pydata.org/generated/seaborn.move_legend.html
# dodaj tytuł, opisz oś x i y (możesz użyć matplotliba)

# df_new = df[df['Type_2'].isnull()]
# print(df_new)
# ax = sns.scatterplot(data=df_new,x='Attack',y='Defense',hue='Stage')
# sns.move_legend(ax, "upper left", bbox_to_anchor=(1,1))
# plt.title("Zależność ataku do obrony")
# plt.ylabel("Obrona")
# plt.xlabel("Atak")
# plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 2

# Wykres słupkowy ma przedstawiać liczbę pokemonów, których podstawowym typem (Type 1) jest typ trawiasy (Grass),
# ognisty (Fire) lub wodny (Water).
#
#     na początku odpowiednio przefiltruj dane, to znaczy wyciągnij informacje wyłacznie o wspomnianych trzech
#     typach pokemonów
#
#     następnie pogrupuj dane względem typu
#
#     wyciągnij informację na temat ilości pokemonów dla każdego z typów
#         podpowiedź: dla ułatwienia zadania - jeśli używasz groupby() i count() - przekonwertuj serię danych
#         na dataframe używając reset_index()
#
#     ustaw kolor słupków zgodnie z typem pokemona - skorzystaj z argumentu palette
#
#         możesz użyć poniższego schematu kolorów
#
#         pkmn_type_colors = ['#F08030','#78C850','#6890F0']
#
#     ustaw etykietę osi x i y, nadaj wykresowi tytuł (możesz użyć matplotlib)

# df_new2 = df[df['Type_1'].isin(['Grass','Water','Fire'])]
# df2 = df[(df['Type_1'] == 'Fire' ) | (df['Type_1'] == 'Grass') | (df['Type_1'] == 'Water')]
#
# dfIlosc = df2.groupby('Type_1')['Total'].count().reset_index()
#
# pkmn_type_colors = ['#F08030','#78C850','#6890F0']
#
# sns.barplot(data=dfIlosc, x='Type_1', y='Total', palette=pkmn_type_colors, hue='Type_1')
#
# plt.title('Ilość pokemonów typu: Grass, Water, Fire')
# plt.ylabel('Liczba')
# plt.xlabel('Typ pokemona')
#
# plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 3

# Wykres kołowy powinien przedstawić jaki procent pokemonów stanowią pokemony legendarne:
#
#     zmień nazwy wartości kolumny "Legendary" z "False"/"True" na "Zwykły"/"Legendarny"
#     wyświetl wartości procentowe na wykresie kołowym stosując parametr autopct
#     nadaj wykresowi tytuł (możesz użyć matplotlib)

# df['Legendary'] = df.apply(lambda x: 'Zwykly' if x['Legendary'] == False else 'Legendarny', axis = 1)
# print(df.head())
#
# x = df.groupby('Legendary')['Legendary'].count()
# plt.title('')
# plt.pie(x, autopct='%1.1f%%', labels=x.index, colors=['#ffb482', '#a1c9f4'])
# plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 4

# Wykres pudełkowy przedstawia rozkład wartości danych dla każdej grupy.
# Pozioma kreska na środku pudełka oznacza medianę, z kolei równoległe do mediany boki
# oznaczają kwartyle - dolny, czyli pierwszy kwartyl oraz górny czyli trzeci kwartyl.
#
# (czym jest kwartyl -> https://pl.wikipedia.org/wiki/Kwartyl)
#
# Wąsy poza boksami przedstawiają dolną i górną granicę danych.
# Pojedyncze punkty poza wąsami przedstawiają wartości odstające (outliers)
#
# Zadanie: Przedstaw statystyki pokemonów w postaci wykresu pudełkowego sns.boxplot().
# Wykorzystaj kolumnę HP, Attack oraz Defence (pamiętaj: do wyciągnięcia kolumn możesz
# użyć m.in. funkcji .loc lub .iloc)
#
#     dodaj tytuł, opisz oś y - możesz skorzystać z biblioteki matplotlib
#     zmień nazwy kolumn, aby oś x wyświetlała się jak na przedstawionym wykresie
#     (podobnie jak w poprzednim wykresie, możesz skorzystać z .set_axis())

# df.head()
#
x = df[['HP','Attack','Defense']]
#
# plt.figure(figsize = (10,6))
sns.boxplot(data=x)
#
# plt.title('Podstawowe statystyki Pokemonów')
# plt.xlabel('Statystyki')
# plt.ylabel('Wartości')
#
# plt.xticks(ticks=[0,1,2], labels=['HP', 'Atak', 'Obrona'])
plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 4

# Wykres przedstawiający główną zależność dwóch zmiennych (x i y)
# oraz zależność opisującą główny wykres. W poniższym przykładzie, wykresem opisującym wykres
# punktowy jest wykres gęstości.
#
# https://seaborn.pydata.org/generated/seaborn.jointplot.html
#
# Przedstaw zależność wartości ataku (Attack) od obrony (Defense) przy
# rozróżnieniu pokemonów na legendarne i zwykłe (kolumna Legendary) używając funkcji sns.jointplot()

sns.jointplot(data=df, x='Attack', y='Defense', hue='Legendary')
plt.show()

#-----------------------------------------------------------------------------------------------------------

#zad 5
# Wykres przedstawiający macierz korelacji - wskazuje na korelację dla odpowiednich par zmiennych losowych. Dla tej samej pary (Attack-Attack, Defense-Defense ...) przedstawione są histogramy, czyli częstości występowania danej cechy (na osi x widać wartości cechy, na y częstość występowania). Wykresy punktowe standardowo przedstawiają zależność jednej cechy od drugiej.
#
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
#
# Stwórz macierz korelacji dla Ataku, Obrony i Szybkości pokemonów:
#
#     wyciągnij odpowiednie kolumny przy pomocy funkcji .loc()
#     zwizualizuj wyżej wymienione statystyki przy pomocy sns.pairplot()

x = df[['Attack', 'Defense', 'Speed']]
sns.pairplot(data=x)
plt.show()
