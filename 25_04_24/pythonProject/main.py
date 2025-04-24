import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

t = np.linspace(0, 2 * np.pi, 100)
z = t
x = np.sin(t)*np.cos(t)
y = np.tan(t)
ax.plot(x, y, z, label='example')
ax.legend()
#plt.show()

# Zadanie 1
# Wygeneruj wykres liniowy dla z od 0 do 2pi, x = sin(z), y = 2cos(z).
t = np.linspace(0, 2 * np.pi, 100)
z = t
x = np.sin(z)
y = np.cos(z)
ax.plot(x, y, z, label='zadanie 1')
ax.legend()
#plt.show()


# Zadanie 2
# Wygeneruj wykres punktowy dla 5 różnych losowych serii z użyciem
# różnych znaczników i kolorów: https://matplotlib.org/api/markers_api.html

# Ustawienia znaczników i kolorów
markers = ['o', 's', '^', 'D', 'x']
colors = ['red', 'green', 'blue', 'orange', 'purple']

# Tworzenie figury i wykresu 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Generowanie i rysowanie 5 serii 3D
for i in range(5):
    x = np.random.rand(10)
    y = np.random.rand(10)
    z = np.random.rand(10)
    ax.scatter(x, y, z, marker=markers[i], color=colors[i], label=f'Seria {i+1}')

ax.set_title('3D wykres punktowy – 5 losowych serii')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()


# Zadanie 3
# Wygeneruj wykres powierzchniowy z przykładu z podpunktu 1.2 w 5 różnych
# dowolnych kolorystkach (wykorzystaj referencje dostępne na
# stronie: https://matplotlib.org/stable/gallery/color/colormap_reference.html)

# Lista kolorystyk
colormaps = ['viridis', 'plasma', 'inferno', 'coolwarm', 'cividis']

# Dane wejściowe (siatka X, Y, funkcja Z)
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Tworzenie 5 wykresów powierzchniowych z różnymi kolorystykami
fig = plt.figure(figsize=(15, 10))

for i in range(5):
    ax = fig.add_subplot(2, 3, i + 1, projection='3d')
    ax.plot_surface(X, Y, Z, cmap=colormaps[i])
    ax.set_title(f'Colormap: {colormaps[i]}')

plt.tight_layout()
plt.show()

# Zadanie 4
# Wygeneruj z pomocą dokumentacji wykres słupkowy z przykładu z podpunktu 1.3
# wykorzystując 4 różne kombinacje wyglądu (z cieniowaniem, bez cieniowania, dowolna kolorystyka)

# set up the figure and Axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Shaded')

ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
ax2.set_title('Not Shaded')

plt.show()