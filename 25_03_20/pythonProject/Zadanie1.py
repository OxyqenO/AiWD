import pandas as pd


#Zadanie 1, 2

df = pd.read_excel('./datasets/imiona.xlsx')

#print(df)


#a)
a = df[df['Liczba'] > 1000]
#print(a)

#b)
b = df[df['Imie'] == 'TINA']
#print(b)

#c)
c = df["Liczba"].sum()
#print(c)

#d)
d = df.groupby(['Rok'])['Liczba'].sum()
#print(d,'\n')

#Zadanie 3

df1 = pd.read_csv("./datasets/zamowienia.csv")
print(df1)

#a)
a1 = df1['Sprzedawca']
print(a1)