import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, CheckButtons, Button


def lissajous(a: float, b: float, delta: float, t: float) -> tuple[float, float]:
    """Генерирует точки для графика Лиссажу в заданный момент времени

    Args:
        a (float): Параметр a лиссажу
        b (float): Параметр b лиссажу
        delta (float): Сдвиг фазы лиссажу
        t (float): Момент времени

    Returns:
        tuple[float, float]: Кортеж, содержащий координаты точки на графике Лиссажу
    """
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y


# Словарь стилей линий, где ключ - это описание стиля, а значение - строка для передачи в Matplotlib
styles = {
    "Красный Сплошная": "red -",
    "Синий Пунктир": "blue --",
    "ЗеленыйШтрихпунктир": "green -.",
}


def get_styles(style: str) -> tuple[str, str]:
    """Возвращает цвет и стиль линии по переданному описанию стиля.

    Args:
        style (str): Описание стиля.

    Returns:
        tuple[str, str]: Кортеж, содержащий цвет и стиль линии.
    """
    color_out: str = "red"
    style_out: str = "-"

    for key in styles:
        if style == key:
            color_out, style_out = styles[key].split(" ")
    return color_out, style_out


if __name__ == "__main__":
    # Размещение радиокнопок для цвета и стиля линии

    def update_graph():
        """Обновляет Фигуру Лиссажу и точку с учетом текущих параметров.

        Args:
            None

        Returns:
            None
        """
        global slider_t, ax, a, b, delta, point, show_tangent, tangent_line, line_style

        ax.clear()

        a, b, delta = 2, 3, np.pi / 3
        t_values = np.linspace(0, 2 * np.pi, 1000)
        x_values, y_values = lissajous(a, b, delta, t_values)

        color_out, style_out = get_styles(line_style)

        (line,) = ax.plot(
            x_values, y_values, label="Лиссажу", color=color_out, linestyle=style_out
        )

        (point,) = ax.plot([], [], "ro", markersize=8)
        (tangent_line,) = ax.plot([], [], "k--")

        # ? Обновляем точку и касательную линию
        t = slider_t.val
        x, y = lissajous(a, b, delta, t)

        point.set_data(x, y)

        if show_tangent:
            slope, intercept = tangent_line_coefficients(a, b, delta, t)
            tangent_line.set_data(
                [-1.5, 1.5], [slope * (-1.5) + intercept, slope * 1.5 + intercept]
            )
        else:
            tangent_line.set_data([], [])

        plt.show()

    def update_point_data(val):
        """Обработчик события изменения значения слайдера времени"""
        update_graph()

    def tangent_line_coefficients(a, b, delta, t):
        """Рассчитываем коэффициенты наклона и пересечения касательной для графика Лиссажу

        Args:
            a (float): Параметр a лиссажу
            b (float): Параметр b лиссажу
            delta (float): Сдвиг фазы лиссажу
            t (float): Момент времени

        Returns:
            tuple[float, float]: Кортеж, содержащий коэффициенты наклона и пересечения касательной
        """
        x, y = lissajous(a, b, delta, t)
        dx_dt = a * np.cos(a * t + delta)
        dy_dt = b * np.cos(b * t)
        slope = dy_dt / dx_dt
        intercept = y - slope * x
        return slope, intercept

    def reset_point(event):
        """Обработчик события при клике на кнопку сброса позиции точки"""
        slider_t.set_val(0)
        update_graph()

    def toggle_tangent(label):
        """Обработчик события при клике на кнопку показа касательной линии"""
        global show_tangent
        show_tangent = not show_tangent
        update_graph()

    def change_line_style(label):
        """Обработчик события при изменении стиля линии"""
        global line_style
        line_style = label
        update_graph()

    # ? Инициализация флагов
    show_tangent: bool = False

    line_style: str = ""

    # ? Инициализация графика
    fig, ax = plt.subplots(figsize=(8, 6))

    # ? Инициализация слайдера времени
    slider_ax_t = plt.axes([0.1, 0.01, 0.65, 0.03])
    slider_t = Slider(slider_ax_t, "Время - t", 0, 2 * np.pi, valinit=0, valstep=0.01)
    slider_t.on_changed(update_point_data)

    # ? Инициализация сброс
    reset_button_ax = plt.axes([0.8, 0.1, 0.1, 0.04])
    reset_button = Button(reset_button_ax, "Сброс")
    reset_button.on_clicked(reset_point)

    # ? Инициализация флага вкл\выкл касательной
    tangent_checkbox_ax = plt.axes([0.8, 0.025, 0.15, 0.04])
    tangent_checkbox = CheckButtons(
        tangent_checkbox_ax, ["Касательная"], actives=[False]
    )

    # # ? Инициализация радиокнопоки цвета и стиля линий
    tangent_checkbox.on_clicked(toggle_tangent)
    radio_buttons_ax_color = plt.axes([0.6, 0.1, 0.3, 0.15])
    radio_buttons_color = RadioButtons(radio_buttons_ax_color, list(styles))
    radio_buttons_color.on_clicked(change_line_style)

    update_graph()
