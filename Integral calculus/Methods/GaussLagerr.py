# -*- coding: utf-8 -*-

import numpy as np
from numpy.polynomial.laguerre import laggauss

# Определение функции, которую нужно проинтегрировать с учётом весовой функции
def GaussLagger(x):
    return np.exp(-x**2)/np.exp(-x)

# Получение узлов и весов для метода Гаусса-Лагерра
n = 100  # Количество узлов
nodes, weights = laggauss(n)

# Вычисление интеграла
integral = np.sum(weights * GaussLagger(nodes))*2

print("Значение интеграла Гаусса методом Лагерра-Гаусса:", integral)