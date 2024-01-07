# -*- coding: utf-8 -*-

import numpy as np
from numpy.polynomial.legendre import leggauss

# Параметры
E = 1 #эВ
h_bar = 6.582119569e-16 # эВ*с
m = 9.10938356e-31 # кг

# Потенциальный барьер
def U(x):
    return 10*x**2  #Пример потенциального барьера

# Волновая функция Липпмана-Швингера
def psi(x, k):
    integral = 0
    x_nodes, weights = leggauss(50)  # Задаём узлы
    for i in range(len(x_nodes)):
        integral += weights[i] * np.exp(1j * k * np.abs(x - x_nodes[i])) * U(x_nodes[i]) * np.exp(1j * k * x_nodes[i])
    return np.exp(1j * k * x) - 1j/(2*k) * 2 * integral

#Считаем коэффициент прохождения в ассимптотике волновой функции
k = np.sqrt(2*m*E) / h_bar
x_large = 100  # Значение x для имитации ассимптотики
psi_large = psi(x_large, k)
T = np.abs(1/psi_large)**2

print("Коэффициент прохождения:", T)