from gui import ChessGUI
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    gui = ChessGUI()
    gui.show()
    app.exec()
