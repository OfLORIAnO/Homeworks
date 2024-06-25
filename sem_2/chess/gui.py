# gui.py
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget,
)

from board import Board
from cell import Cell


class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Chess")
        self.setGeometry(100, 100, 800, 800)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        self.central_widget.setStyleSheet("background-color: #EEA26E")
        self.init_render()

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
