# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

U0 = 0.25  # в электронвольтах
alpha = 15e-10  # в метрах

# Константы
h_bar = 6.58212e-16  # постоянная Планка в электронвольтах*с
m = 9.10938356e-31  # масса электрона в кг

# Функция для вычисления коэффициента прохождения T(E)
def T(E):
    T_values = []
    for energy in E:
        k = np.sqrt(2 * m * energy) / h_bar
        k0 = np.sqrt(2 * m * U0) / h_bar
        kappa = np.sqrt(k0**2 - k**2)
        T_result = 1 / (1 + (k0**2 / (2 * kappa * k))**2 * np.sinh(kappa * alpha)**2*10**17)
        T_values.append(T_result)
        print(T_result)
    return T_values

# Массив значений энергии E
E_values = np.arange(0, 0.2, 0.005)  # масштаб энергий

# Значения коэффициента прохождения T для каждой энергии E
T_values = T(E_values)

# Строим график T(E)
plt.plot(E_values, T_values)
plt.xlabel('E (эВ)')
plt.ylabel('T')
plt.title('График T(E)')
plt.show()
