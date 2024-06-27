# gui.py
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
)
from board import Board


class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.StartUI()

    def StartUI(self):
        # ? Создание центрального виджета
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("background-color: #EEA26E")
        self.setWindowTitle("Chess")
        self.setGeometry(100, 100, 800, 800)
        self.setCentralWidget(self.central_widget)
        # ? Создание основного вертикального макета
        self.main_layout = QVBoxLayout()

        # Board layout
        self.board_layout = QGridLayout()
        self.init_render()

        # Создание горизонтального макета (QHBoxLayout)
        self.hbox_layout = QHBoxLayout()

        buttonStart = QPushButton("Найти решения")
        buttonStart.setStyleSheet("background-color: green; color: white;")
        buttonStart.clicked.connect(self.board.start_solve)
        self.hbox_layout.addWidget(buttonStart)

        L_input = QLineEdit()
        L_input.setPlaceholderText("Количество фигур, необходимое расставить")
        L_input.textChanged.connect(
            lambda: self.board.change_L(L_input.text(), L_input)
        )
        L_input.setText(str(self.board.L))
        self.hbox_layout.addWidget(L_input)

        self.main_layout.addLayout(self.board_layout)
        self.main_layout.addLayout(self.hbox_layout)
        self.central_widget.setLayout(self.main_layout)

    def init_render(self):
        for x in range(self.board.N):
            for y in range(self.board.N):
                cell = self.board.get_cell(x, y)
                if cell:
                    self.board_layout.addWidget(cell.button, x, y)


if __name__ == "__main__":
    app = QApplication([])
    gui = ChessGUI()
    gui.show()
    app.exec()
