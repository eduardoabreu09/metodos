"""
Script que tenta encontrar todos os intervalos contendo
raízes de uma função. O script recebe como entrada
(nessa ordem):
f: a expressão matemática (string) que está sendo analisada;
a: extremo esquerdo do intervalo;
b: extremo direito do intervalo;
dx: Incremento usado na busca por raízes.

Exemplo de uso:
python3 rootfinder.py "x**3 - 9*x + 3" -5 5 0.5

César Lincoln Cavalcante Mattos - 2018
"""

import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import findroots as fr

mpl.rcParams['lines.linewidth'] = 2

f = lambda x: eval(sys.argv[1])

a = float(sys.argv[2])
b = float(sys.argv[3])
dx = float(sys.argv[4])

fig, ax = plt.subplots()
plt.xlabel("x")
plt.ylabel("fx")
plt.title("Esboço da função f(x)")
xRange = np.arange(a, b, 0.01)
fxRange = f(xRange)
ax.set(xlim=(a, b), ylim=(min(fxRange), max(fxRange)))
ax.plot(xRange, fxRange, 'b-', xRange, 0*xRange, 'k-')[0]

intervals = []
while True:
    x1,x2 = fr.findroots(f,a,b,dx)
    if x1 != None:
        a = x2
        intervals.append([x1, x2])
    else:
        break

intervals = np.array(intervals)
vertSize = int(0.15*max(abs(fxRange)))
print(vertSize)
for i in range(intervals.shape[0]):
    ax.plot(vertSize*[intervals[i,0]], np.arange(vertSize)-vertSize/2, 'r-')
    ax.plot(vertSize*[intervals[i,1]], np.arange(vertSize)-vertSize/2, 'r-')
    ax.plot(np.linspace(intervals[i,0], intervals[i,1], num=10), 10*[0], 'r-')

print("Intervalos encontrados:")
print(intervals)
plt.show()
