import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# Определение функции
def f(x):
    return np.cos(x) * np.sin(x**2 + 8)


# Определение производной функции
def df(x):
    return 2 * x * np.cos(x) * np.cos(x**2 + 8) - np.sin(x) * np.sin(x**2 + 8)


def df2(x):
    return (-4 * x**2 - 1) * np.cos(x) * np.sin(x**2 + 8) + (
        2 * np.cos(x) - 4 * x * np.sin(x)
    ) * np.cos(x**2 + 8)


# Задание интервала
x_values = np.linspace(0, 5, 1000)
y_values = f(x_values)

# 1. График функции
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="График функции")
plt.title("График функции")
plt.show()

# 2. Графики первой и второй производных
plt.figure(figsize=(8, 6))
plt.plot(x_values, df(x_values), label="Первая производная")
plt.title("Первая производная")
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(x_values, df2(x_values), label="Вторая производная")
plt.title("Вторая производная")
plt.show()

# 3. Графики касательной и нормали
min_index = np.argmin(y_values)
min_point = (x_values[min_index], y_values[min_index])
x0, y0 = min_point

tangent_equation = lambda x: y0 + df(x0) * (x - x0)
normal_equation = lambda x: y0 - 1 / df(x0) * (x - x0)

plt.figure(figsize=(8, 6))
plt.plot(x_values, f(x_values), label="График функции")
plt.plot(x_values, tangent_equation(x_values), "--", label="Касательная")
plt.plot(x_values, normal_equation(x_values), "--", label="Нормаль")
plt.plot(x0, y0, "ro")  # Точка касания
plt.title("Касательная и нормаль")
plt.legend()
plt.show()

# 4. Касательное расслоение для 10 точек
# Задание интервала
num_points = 1000  # Количество точек для построения касательных
x_values = np.linspace(0, 5, num_points)


# Функция для построения касательного расслоения в заданной точке x_o
def tangent_lines(x_o):
    return f(x_o) + df(x_o) * (x_values - x_o)


# Построение графика функции
plt.figure(figsize=(8, 6))
plt.plot(x_values, f(x_values), label="График функции")

# Построение касательного расслоения для нескольких точек
for x in np.linspace(0, 5, 5):  # Выберите нужное количество точек для отображения
    plt.plot(x_values, tangent_lines(x), "--", alpha=0.3)

plt.title("Касательное расслоение")
plt.legend()
plt.show()

# 5. Длина кривой через интеграл
curve_length, _ = integrate.quad(lambda x: np.sqrt(1 + df(x) ** 2), 0, 5)

print(f"Длина кривой: {curve_length:.2f}")
