import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import yscale

df = pd.read_excel("./datasets/imiona.xlsx")
print(df, '\n\n')

#zadanie 1
data = df.groupby('Rok')['Liczba'].sum()

data = data / 1000
#print(data)
#data.plot(title='Liczba narodzin w każdym roku', figsize=(8,6), grid=True, ylabel='Liczba narodziny [tys.]', xlabel='Rok', rot=45, xticks=data.index)
#plt.show()

#zadanie 2

#data2 = df.groupby('Plec')['Liczba'].sum()
#data2.plot.bar(title='Tytuł', rot=45, figsize=(10,10), ylabel='Ilość', xlabel='Płeć')
#plt.show()

#zadanie 3

data3 = df.groupby('Plec')['Liczba'].sum()
data3.plot.pie(title='Płeć',subplots=True, autopct='%.2f %%')
plt.show()