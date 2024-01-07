# -*- coding: utf-8 -*-

import numpy as np
from numpy.polynomial.legendre import leggauss

# Определение функции, которую нужно проинтегрировать
def GaussLeg(x):
    return np.exp(-(x**2))

# Получение узлов и весов для метода Лежандра-Гаусса
n = 100  # Количество узлов
nodes, weights = leggauss(n)  

# Преобразование узлов от -1 до 1 к узлам с бесконечными пределами
t_nodes = nodes / (1 - nodes**2)
transformed_weights = (1 + nodes**2) / (1 - nodes**2)**2 * weights

# Вычисление интеграла с бесконечными пределами
integral_value = np.sum(transformed_weights * GaussLeg(t_nodes))

print("Значение интеграла Гаусса методом Лежандра-Гаусса:", integral_value)