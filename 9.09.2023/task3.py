emptySymbol = "∙"
def inputData():
    word = input("Введите слово: ")
    row = int(input("Введите кол-во строк: "))
    return word, row
def printTable(table):
    cnt = 0
    for row in table:
        cnt += 1
        print(row)
def createTable(row): #? Создаём таблицу
    table = []
    for _ in range(row):
        table.append(emptySymbol)
    return table
def addRightCell(table):#Расширяем таблицу вправо
    tempTable = []
    for row in table:
        row += emptySymbol
        tempTable.append(row)
    return tempTable
def addLetter(table, posY, posX, letter, mode): #? Меняем значение символа на заданной клетке
    if mode == 'diag': #? Если мы идём по диагонали, то расширяем таблицу вправо
        table = addRightCell(table) 
    row = table[posY]
    rowTemp = []
    for symbol in row:
        rowTemp.append(symbol)
    row = rowTemp
    row[posX] = letter
    table[posY] = "".join(row)
    return table

def Program(word="Программирование", row=3):
    #? initialization
    # word, row = inputData()
    mode = "vert" #! "vert" | "diag" ("vert" - default)
    table = createTable(row)
    posX = posY = 0 #? Начальные координаты
    cntY = row #? Счётсик спусков вниз (по posY)

    if row <= 1: 
        print(word)
        return 

    for i in range(len(word)):
        letter = word[i]
        if mode == "vert": #? Если вертикальный режим, то 
            cntY -= 1
            table = addLetter(table, posY, posX, letter, mode)
            if cntY <= 0: #? Если мы дошли до нижней ячейки
                mode = "diag" #? меняем на diag
                posY -= 1 #? Прыгаем на клетку наверх
                posX += 1 #? Прыгаем на клетку вправо
                cntY = row - 1 #? Обновляем счётчик, но уже с учётом прыжка
            else:
                posY += 1 #? Прыгаем на клетку вниз
        else:
            cntY -= 1 
            table = addLetter(table, posY, posX, letter, mode)
            if cntY <= 0: #? Если мы дошли до верхнй ячейки
                mode = "vert" #? меняем на vert
                posY += 1 #? Прыгаем на клетку вниз
                cntY = row - 1  #? Обновляем счётчик с учётом прыжка
            else:
                posX += 1 #? Прыгаем на клетку вправо
                posY -= 1 #? Прыгаем на клетку наверх

    printTable(table)
if __name__ == "__main__":
    print('*'*10)
    Program("Оптимистичность", 4)
    print('*'*10)
    Program("Программирование", 5)
    print('*'*10)
    Program("Программирование", 6)
    print('*'*10)
    Program("Технологии", 3)
    print('*'*10)
    Program("Математика", 2)
    print('*'*10)
    Program("Математика", 1)
    print('*'*10)
    Program("♡"*21, 5)
    print('*'*10)