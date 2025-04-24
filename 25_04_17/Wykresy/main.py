import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zadanie 1
# Stwórz i wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20].
# Opisz linię wykresu dodając legendę z etykietą f(x) = 1/x. Dodaj odpowiednie etykiety do
# obu osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (0, długość wektora x).

x = np.arange(20) + 1
y = 1/x

plt.plot(x, y, label='f(x) = 1/x')
plt.ylabel('f(x)')
plt.xlabel('x')

plt.axis([0,20,0,1])

plt.legend()

plt.show()
