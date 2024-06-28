# gui.py
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)
from board import Board
from solutionGUI import SolutionsGUI
from dialog import Dialog
from color import Color
from input import Input


class StartGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.StartUI()

    def __on_click_on_solve(self):
        self.board.start_solve()

        if len(Board.total_solutions) == 0:
            Dialog("Не найдено решений", Color.red)
            self.close()
            return

        self.new_window = SolutionsGUI()
        Dialog("количество решений:" + str(len(Board.total_solutions)), Color.green)
        self.close()
        self.new_window.show()

    def StartUI(self):
        # ? Создание центрального виджета
        self.board = Board()
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("background-color: #EEA26E")
        self.setWindowTitle("Chess")
        self.setGeometry(100, 100, 800, 800)
        self.setCentralWidget(self.central_widget)
        # ? Создание основного вертикального макета

        self.main_layout = QVBoxLayout()
        self.hbox_layout = QHBoxLayout()

        buttonStart = QPushButton("Найти решения")
        buttonStart.setStyleSheet("background-color: green; color: white;")
        buttonStart.clicked.connect(self.__on_click_on_solve)

        L_Label = QLabel("Количество фигур, необходимое расставить")
        L_input = Input()
        L_input.setPlaceholderText("Количество фигур, необходимое расставить")
        L_input.textChanged.connect(
            lambda: self.board.change_L(L_input.text(), L_input)
        )
        L_input.setText(str(self.board.L))

        self.hbox_layout.addWidget(L_Label)
        self.hbox_layout.addWidget(L_input)
        self.hbox_layout.addWidget(buttonStart)

        self.main_layout.addLayout(self.board)
        self.main_layout.addLayout(self.hbox_layout)

        self.central_widget.setLayout(self.main_layout)
