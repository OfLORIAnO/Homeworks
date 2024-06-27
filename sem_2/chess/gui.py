# gui.py
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget,
    QPushButton,
    QLineEdit,
)
from board import Board


class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.StartUI()

    def StartUI(self):
        # ? Layout
        self.setWindowTitle("Chess")
        self.setGeometry(100, 100, 800, 800)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        self.central_widget.setStyleSheet("background-color: #EEA26E")

        self.board = Board()
        self.init_render()

        # ? кнопка "Найти решения"
        self.buttonStart = QPushButton("Найти решения")
        self.buttonStart.setStyleSheet("background-color: green; color: white;")
        self.buttonStart.clicked.connect(self.board.start_solve)
        self.grid_layout.addWidget(self.buttonStart, 0, 999)

        # ? Input того, сколько фигур нужно расставить
        self.L_input = QLineEdit(self)
        self.L_input.placeholderText = "Количество фигур, необходимое расставить"
        self.L_input.textChanged.connect(self.board.confirm_L)
        self.L_input.text = self.board.L
        self.grid_layout.addWidget(self.L_input, 1, 999)

    def init_render(self):
        for x in range(self.board.N):
            for y in range(self.board.N):
                cell = self.board.get_cell(x, y)
                if cell:
                    self.grid_layout.addWidget(cell.button, x, y)

    def render(self):
        for x in range(self.board.N):
            for y in range(self.board.N):
                self.board.get_cell(x, y).render()


if __name__ == "__main__":
    app = QApplication([])
    gui = ChessGUI()
    gui.show()
    app.exec()
