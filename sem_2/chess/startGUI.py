# Импорт необходимых классов и виджетов из библиотеки PySide6
from PySide6.QtWidgets import (
    QMainWindow,  # Основное окно приложения
    QWidget,  # Базовый виджет
    QPushButton,  # Кнопка
    QLabel,  # Метка текста
    QVBoxLayout,  # Вертикальный макет
    QHBoxLayout,  # Горизонтальный макет
)

# Импорт пользовательских модулей и классов
from board import Board  # Класс для представления доски (вероятно, шахматной)
from solutionGUI import SolutionsGUI  # Класс для отображения решений
from dialog import Dialog  # Класс для создания диалоговых окон
from color import Color  # Класс для определения цветов
from input import Input  # Класс для пользовательского ввода


# Определение класса основного графического интерфейса приложения
class StartGUI(QMainWindow):
    def __init__(self):
        super().__init__()  # Вызов конструктора базового класса QMainWindow
        self.StartUI()  # Инициализация пользовательского интерфейса

    def StartUI(self):
        # Создание центрального виджета
        self.board = Board()  # Создание экземпляра доски
        self.central_widget = QWidget()  # Создание центрального виджета
        self.central_widget.setStyleSheet("background-color: #EEA26E")  # Установка фона
        self.setWindowTitle("Chess")  # Установка заголовка окна
        self.setGeometry(100, 100, 800, 800)  # Установка размеров и позиции окна
        self.setCentralWidget(self.central_widget)  # Установка центрального виджета

        # Создание основного вертикального макета
        self.main_layout = QVBoxLayout()  # Основной вертикальный макет
        self.hbox_layout = QHBoxLayout()  # Горизонтальный макет для кнопки и ввода

        # Создание кнопки для начала поиска решений
        buttonStart = QPushButton("Найти решения")
        buttonStart.setStyleSheet(
            "background-color: green; color: white;"
        )  # Стилизация кнопки
        buttonStart.clicked.connect(
            self.__on_click_on_solve
        )  # Привязка обработчика нажатия

        # Создание метки и поля ввода для количества фигур
        L_Label = QLabel("Количество фигур, необходимое расставить")
        L_input = Input()  # Поле ввода
        L_input.setPlaceholderText(
            "Количество фигур, необходимое расставить"
        )  # Заполнитель текста
        L_input.textChanged.connect(
            lambda: self.board.change_L(L_input.text(), L_input)
        )  # Обновление количества фигур при изменении текста
        L_input.setText(str(self.board.L))  # Установка начального текста

        # Добавление метки, поля ввода и кнопки в горизонтальный макет
        self.hbox_layout.addWidget(L_Label)
        self.hbox_layout.addWidget(L_input)
        self.hbox_layout.addWidget(buttonStart)

        # Добавление доски и горизонтального макета в основной вертикальный макет
        self.main_layout.addLayout(self.board)
        self.main_layout.addLayout(self.hbox_layout)

        # Установка основного макета на центральный виджет
        self.central_widget.setLayout(self.main_layout)

    def __on_click_on_solve(self):
        # Обработчик нажатия кнопки "Найти решения"
        self.board.start_solve()  # Запуск решения задачи

        # Если решения не найдены, отображение диалогового окна и закрытие приложения
        if len(Board.total_solutions) == 0:
            Dialog(
                "Не найдено решений", Color.red
            )  # Отображение сообщения об отсутствии решений
            self.close()  # Закрытие основного окна
            return

        # Если решения найдены, создание нового окна для отображения решений
        self.new_window = SolutionsGUI()
        Dialog(
            "количество решений: " + str(len(Board.total_solutions)), Color.green
        )  # Отображение количества решений
        self.close()  # Закрытие основного окна
        self.new_window.show()  # Показ нового окна с решениями
