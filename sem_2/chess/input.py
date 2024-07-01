from PySide6.QtWidgets import QLineEdit


class Input(QLineEdit):
    def __init__(self, parent=None):
        """
        Получение текста из поля ввода.

        Возвращаемое значение:
        - str: Текущий текст, введенный в поле ввода.
        """
        super().__init__(parent)

    def get_text(self) -> str:
        return self.text()
