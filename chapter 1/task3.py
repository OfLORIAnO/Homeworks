from typing import Tuple, Literal, Union

emptySymbol: str = " "


def inputData() -> Tuple[str, int]:
    """
    Запрашивает у пользователя ввод слова и количества строк.

    Returns:
    - Tuple[str, int]: Кортеж, содержащий введенное слово и количество строк.
    """
    word: str = input("Введите слово: ")
    row: int = int(input("Введите количество строк: "))
    return word, row


def printTable(table: list[str]) -> None:
    """
    Выводит таблицу на экран.

    Args:
    - table (list[str]): Список строк, представляющих таблицу.
    """
    cnt: int = 0
    for row in table:
        cnt += 1
    newString = ""
    for row in table:
        newString += "".join(row.split(emptySymbol))
    print(newString)


def createTable(row: int) -> list[str]:
    """
    Создает таблицу заданного размера.

    Args:
    - row (int): Количество строк в таблице.

    Returns:
    - list[str]: Список строк, представляющих таблицу.
    """
    table: list[str] = []
    for _ in range(row):
        table.append(emptySymbol)
    return table


def addRightCell(table: list[str]) -> list[str]:
    """
    Расширяет таблицу, добавляя пустую ячейку справа к каждой строке.

    Args:
    - table (list[str]): Список строк, представляющих таблицу.

    Returns:
    - list[str]: Список строк с добавленными пустыми ячейками.
    """
    tempTable: list[str] = []
    for row in table:
        row += emptySymbol
        tempTable.append(row)
    return tempTable


def addLetter(
    table: list[str], posY: int, posX: int, letter: str, mode: Literal["vert", "diag"]
) -> list[str]:
    """
    Заменяет значение символа в заданной ячейке таблицы.

    Args:
    - table (list[str]): Список строк, представляющих таблицу.
    - posY (int): Индекс строки.
    - posX (int): Индекс столбца.
    - letter (str): Символ, который следует добавить в ячейку.
    - mode (Literal["vert", "diag"]): Режим работы ("vert" - вертикальный, "diag" - диагональный).

    Returns:
    - list[str]: Измененный список строк.
    """
    if mode == "diag":
        table = addRightCell(table)
    row: Union[str, list[str]] = table[posY]
    rowTemp: list[str] = []
    for symbol in row:
        rowTemp.append(symbol)
    row = rowTemp
    row[posX] = letter
    table[posY] = "".join(row)
    return table


def Program(word: Union[str, bool] = False, row: int = 3) -> Union[bool, None]:
    """
    Основная программа, создающая и заполняющая таблицу в соответствии с введенным словом.

    Args:
    - word (Union[str, bool]): Слово, которое следует использовать для заполнения таблицы.
    - row (int): Количество строк в таблице (по умолчанию 3).

    Returns:
    - Union[bool, None]: Возвращает False, если пользователь ввел некорректные данные, в противном случае возвращает None.
    """
    if type(word) == bool:
        word, row = inputData()

    # Инициализация
    mode: Literal["vert", "diag"] = "vert"
    table: list[str] = createTable(row)
    posX: int = 0  # Начальные координаты
    posY: int = 0
    cntY: int = row  # Счетчик спусков вниз (по posY)

    if row <= 1:
        if row <= 0:
            print("Вы чё там, совсем с ума сошли?")
            return False
        print(word)
        return None

    for i in range(len(word)):
        letter: str = word[i]
        if mode == "vert":
            cntY -= 1
            table = addLetter(table, posY, posX, letter, mode)
            if cntY <= 0:
                mode = "diag"
                posY -= 1
                posX += 1
                cntY = row - 1
            else:
                posY += 1
        else:
            cntY -= 1
            table = addLetter(table, posY, posX, letter, mode)
            if cntY <= 0:
                mode = "vert"
                posY += 1
                cntY = row - 1
            else:
                posX += 1
                posY -= 1
    printTable(table)
    return None


if __name__ == "__main__":
    Program("Оптимистичность", 4)
    Program("Программирование", 5)
    Program("Программирование", 6)
    Program("Технологии", 3)
    Program("Математика", 2)
    Program("♡" * 21, 5)
