# gui.py
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
)
from board import Board


class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
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
        self.hbox_layout = QVBoxLayout()

        self.board = Board([(0, 0), (6, 7)])

        buttonStart = QPushButton("Найти решения")
        buttonStart.setStyleSheet("background-color: green; color: white;")
        buttonStart.clicked.connect(self.board.start_solve)

        L_Label = QLabel("Количество фигур, необходимое расставить")
        L_input = QLineEdit()
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


if __name__ == "__main__":
    app = QApplication([])
    gui = ChessGUI()
    gui.show()
    app.exec()
