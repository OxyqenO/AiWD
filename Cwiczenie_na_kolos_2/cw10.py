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
df['Legendary'] = df.apply(lambda x: 'Zwykly' if x['Legendary'] == False else 'Legendarny', axis = 1)
print(df.head())

x = df.groupby('Legendary')['Legendary'].count()
plt.title('')
plt.pie(x, autopct='%1.1f%%', labels=x.index, colors=['#ffb482', '#a1c9f4'])
plt.show()
