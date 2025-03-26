import numpy as np
import pandas as pd

#Zadanie 1, 2

df = pd.read_excel('./datasets/imiona.xlsx')

print('zadanie 1\n',df,'\n\n')

#a)
a = df[df['Liczba'] > 1000]
print('a)\n',a,'\n\n')

#b)
b = df[df['Imie'] == 'TINA']
print('b)\n',b,'\n\n')

#c)
c = df["Liczba"].sum()
print('c)\n',c,'\n\n')

#d)
d = df.groupby(['Rok'])['Liczba'].sum()

print('d)\n',d,'\n\n')

e = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)].groupby('Rok')['Liczba'].sum()

print('e)\n',e,'\n\n')

f = df.groupby(['Rok', 'Plec'])['Liczba'].sum()
print('f)\n',f,'\n\n')

g = df.groupby('Plec').head(1)
g2 = df.groupby('Plec').tail(1)
print('g)\n',g,'\n\n',g2)

h = df.groupby(['Rok', 'Plec'])['Liczba'].sum()
print('h)\n',h,'\n\n')



#Zadanie 3

df1 = pd.read_csv("./datasets/zamowienia.csv", sep=';')
print('zadanie 2\n',df1,'\n\n')

#a)
a1 = df1.groupby(['Sprzedawca']).nunique()
print('a)\n',a1,'\n\n')

#b)

b1 =  df1.sort_values('Utarg', ascending=0)['Utarg'].head(5)
print('b)\n',b1,'\n\n')

#c) nie działa
c1 = df1.groupby('Sprzedawca')['idZamowienia'].count()
print('c)\n',c1,'\n\n')

#d)
d1 = df1.groupby('Kraj')['idZamowienia'].count()
print('d)\n',d1,'\n\n')