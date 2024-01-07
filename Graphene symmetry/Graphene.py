# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Параметры
a = 1.42  # A
t = -3  # эВ

# Вектора решетки
a1 = np.array([np.sqrt(3)*a/2, a/2])
a2 = np.array([-np.sqrt(3)*a/2, a/2])

# Вектора химических связей
delta1 = a * np.array([-np.sqrt(3)/2, -1/2])
delta2 = a * np.array([np.sqrt(3)/2, -1/2])
delta3 = a * np.array([0, 1])

# Вектора обратной решетки
b1 = 2*np.pi/(3*a) * np.array([np.sqrt(3), -1])
b2 = 2*np.pi/(3*a) * np.array([np.sqrt(3), 1])

# Функция f(k)
def f(kx, ky):
    return np.exp(1j*ky*a) + 2*np.exp(-1j*ky*a/2)*np.cos(np.sqrt(3)*kx*a/2)

# Гамильтониан
def hamiltonian(kx, ky):
    return np.array([[0, t*f(kx, ky)], [t*f(kx, ky).conjugate(), 0]])

# Расчет энергии
kx = np.linspace(-np.pi/(np.sqrt(3)*a), np.pi/(np.sqrt(3)*a), 100)
ky = np.linspace(-np.pi/a, np.pi/a, 100)
energy = np.zeros((len(kx), len(ky)))

for i in range(len(kx)):
    for j in range(len(ky)):
        energy[i, j] = np.linalg.eigvalsh(hamiltonian(kx[i], ky[j]))[0]

# Построение зонной структуры
plt.figure()
plt.contourf(kx, ky, energy, levels=100, cmap='jet')
plt.colorbar(label='Energy (eV)')
plt.xlabel('$k_x$')
plt.ylabel('$k_y$')
plt.title('Graphene Band Structure')
plt.show()