from typing import Tuple, Literal, Union

emptySymbol: str = " "

def inputData() -> Tuple[str, int]:
    word: str = input("Введите слово: ")
    row: int = int(input("Введите кол-во строк: "))
    return word, row


def printTable(table) -> None:
    cnt: int = 0
    for row in table:
        cnt += 1
        # print(row)
    newString = ""
    for row in table:
        newString += "".join(row.split(emptySymbol))
    print(newString)


def createTable(row) -> list[str]:  # ? Создаём таблицу
    table: list[str] = []
    for _ in range(row):
        table.append(emptySymbol)
    return table


def addRightCell(table) -> list[str]:  # ? Расширяем таблицу вправо
    tempTable: list[str] = []
    for row in table:
        row += emptySymbol
        tempTable.append(row)
    return tempTable


def addLetter(table: list[str], posY: int, posX: int, letter: str, mode: Literal["vert", "diag"]) -> list[str]:  # ? Меняем значение символа на заданной клетке
    if mode == "diag":  # ? Если мы идём по диагонали, то расширяем таблицу вправо
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
    if (type (word) == bool) :  # ? Если пользователь не ввёл данные на вход, то заставить его ввести данные
        word, row = inputData()
    # ? initialization
    mode: Literal["vert", "diag"]  = "vert" 
    table: list[str] = createTable(row)
    posX: int = 0  # ? Начальные координаты
    posY: int= 0
    cntY: int = row  # ? Счётсик спусков вниз (по posY)

    if row <= 1:
        if row <= 0:
            print("Вы чё там, совмеи с ума сошли?")
            return False
        print(word)
        return None

    for i in range(len(word)):
        letter: str = word[i]
        if mode == "vert":  # ? Если вертикальный режим, то
            cntY -= 1
            table = addLetter(table, posY, posX, letter, mode)
            if cntY <= 0:  # ? Если мы дошли до нижней ячейки
                mode = "diag"  # ? меняем на diag
                posY -= 1  # ? Прыгаем на клетку наверх
                posX += 1  # ? Прыгаем на клетку вправо
                cntY = row - 1  # ? Обновляем счётчик, но уже с учётом прыжка
            else:
                posY += 1  # ? Прыгаем на клетку вниз
        else:
            cntY -= 1
            table = addLetter(table, posY, posX, letter, mode)
            if cntY <= 0:  # ? Если мы дошли до верхнй ячейки
                mode = "vert"  # ? меняем на vert
                posY += 1  # ? Прыгаем на клетку вниз
                cntY = row - 1  # ? Обновляем счётчик с учётом прыжка
            else:
                posX += 1  # ? Прыгаем на клетку вправо
                posY -= 1  # ? Прыгаем на клетку наверх
    printTable(table)
    return None


if __name__ == "__main__":
    Program("Оптимистичность", 4)
    Program("Программирование", 5)
    Program("Программирование", 6)
    Program("Технологии", 3)
    Program("Математика", 2)
    Program("♡" * 21, 5)
