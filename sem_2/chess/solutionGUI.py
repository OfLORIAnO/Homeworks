# gui.py
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from board import Board


class SolutionsGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SolutionsUI()

    # ? выводит все решения в output.txt
    def __onClick_on_save(self):
        total_solutions = Board.total_solutions
        with open("sem_2/chess/output.txt", "w") as output_file:
            output_file.seek(0)  # ? Очищаем файл
            if not len(total_solutions):
                output_file.write("no solutions")
            else:
                for solution in total_solutions:
                    output_file.write(" ".join([str(elem) for elem in solution]) + "\n")

    def SolutionsUI(self):
        # ? Создание центрального виджета
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("background-color: #EEA26E")
        self.setWindowTitle("Chess")
        self.setGeometry(100, 100, 800, 800)
        self.setCentralWidget(self.central_widget)
        # ? Создание основного вертикального макета

        board = Board([], Board.pick_one_solution(Board.total_solutions))

        buttonStart = QPushButton("Вынести решение в output.txt")
        buttonStart.setStyleSheet("background-color: green; color: white;")
        buttonStart.clicked.connect(self.__onClick_on_save)

        self.main_layout = QVBoxLayout()
        self.hbox_layout = QVBoxLayout()

        self.hbox_layout.addWidget(buttonStart)

        self.main_layout.addLayout(board)
        self.main_layout.addLayout(self.hbox_layout)

        self.central_widget.setLayout(self.main_layout)
