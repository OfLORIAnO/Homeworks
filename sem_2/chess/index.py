from PySide6.QtWidgets import QApplication
import sys

from start import StartGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_window = StartGUI()
    start_window.show()
    sys.exit(app.exec())
