# -*- coding: utf-8 -*-
import numpy as np

def f(x):
    return np.exp(-x**2)

def rectangle_method(a, b, N):
    integral = 0
    dx = (b - a) / N
    for i in range(N):
        x_i = a + (i + 0.5) * dx
        integral += f(x_i)
    integral *= dx
    return integral

a = -10  # нижний предел интегрирования
b = 10   # верхний предел интегрирования
N = 20 # количество прямоугольников

result = rectangle_method(a, b, N)
print("Значение интеграла Гаусса:", result)

