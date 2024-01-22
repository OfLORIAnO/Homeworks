import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, CheckButtons, Button


def lissajous(a, b, delta, t):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y


# Размещение радиокнопок для цвета и стиля линии
colors = {"Красный": "red", "Синий": "blue", "Зеленый": "green"}
styles = {"Сплошная": "-", "Пунктир": "--", "Штрихпунктир": "-."}


def update_graph(val):
    global point, tangent_line
    t = slider_t.val
    x, y = lissajous(a, b, delta, t)

    point.set_data(x, y)

    if show_tangent:
        tangent_line.set_data([0, x], [0, y])
    else:
        tangent_line.set_data([], [])

    fig.canvas.draw_idle()


def reset_point(event):
    slider_t.set_val(0)


def toggle_tangent(label):
    global show_tangent
    show_tangent = not show_tangent


def change_line_style(label):
    line.set_linestyle(styles[label])
    fig.canvas.draw_idle()


def change_line_color(label):
    line.set_color(colors[label])
    fig.canvas.draw_idle()


a, b, delta = 2, 3, np.pi / 2  # Параметры фигуры Лиссажу
t_values = np.linspace(0, 2 * np.pi, 1000)
x_values, y_values = lissajous(a, b, delta, t_values)

fig, ax = plt.subplots(figsize=(8, 6))
(line,) = ax.plot(x_values, y_values, label="Лиссажу")

(point,) = ax.plot([], [], "ro", markersize=8)
(tangent_line,) = ax.plot([], [], "k--")

# Инициализация параметров
show_tangent = False

# Размещение слайдера
slider_ax_t = plt.axes([0.1, 0.01, 0.65, 0.03])
slider_t = Slider(slider_ax_t, "Время", 0, 2 * np.pi, valinit=0, valstep=0.01)
slider_t.on_changed(update_graph)

# Размещение кнопки сброса
reset_button_ax = plt.axes([0.8, 0.1, 0.1, 0.04])
reset_button = Button(reset_button_ax, "Сброс")
reset_button.on_clicked(reset_point)

# Размещение флажка
tangent_checkbox_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
tangent_checkbox = CheckButtons(tangent_checkbox_ax, ["Касательная"], actives=[False])
tangent_checkbox.on_clicked(toggle_tangent)

# ? Радиокнопки на изменение цвета линии
radio_buttons_ax_color = plt.axes([0.8, 0.2, 0.1, 0.15])
radio_buttons_color = RadioButtons(radio_buttons_ax_color, list(colors.keys()))
radio_buttons_color.on_clicked(change_line_color)

# ? Радиокнопки на изменение стиля линии
radio_buttons_ax_style = plt.axes([0.8, 0.35, 0.1, 0.15])
radio_buttons_style = RadioButtons(radio_buttons_ax_style, list(styles.keys()))
radio_buttons_style.on_clicked(change_line_style)

plt.show()
