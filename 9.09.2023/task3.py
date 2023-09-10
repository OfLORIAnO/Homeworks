def printTable(table):
    cnt = 0
    for row in table:
        cnt += 1
        print(cnt, row)
def createTable(row): #? Создаём таблицу
    table = []
    for _ in range(row):
        table.append(" "*20)
    return table
def inputData():
    word = input("Введите слово: ")
    row = int(input("Введите кол-во строк: "))
    
    return word, row
def addLetter(table, posY, posX, letter): #? Меняем значение символа на заданной клетке
    row = table[posY]
    rowTemp = []
    for symbol in row:
        rowTemp.append(symbol)
    row = rowTemp
    row[posX] = letter
    table[posY] = "".join(row)
    return table


def Program():
    word, row = inputData()
    mode = "vert" #! "vert" | "diag" ("vert" - default)
    table = createTable(row)
    posX = posY = 0 #? Начальные координаты
    cntY = row #? Счётсик спусков 

    for i in range(len(word)):
        letter = word[i]
        if mode == "vert": #? Если вертикальный режим, то 
            cntY -= 1
            table = addLetter(table, posY, posX, letter)
            if cntY == 0: #? Если мы дошли до нижней ячейки
                mode = "diag" #? меняем на diag
                posY -= 1 #? Прыгаем на клетку наверх
                posX += 1 #? Прыгаем на клетку вправо
                cntY = row - 1 #? Обновляем счётчик с учётом прыжка
            else:
                posY += 1 #? Прыгаем на клетку вниз
        else:
            cntY -= 1 
            table = addLetter(table, posY, posX, letter)
            if cntY == 0: #? Если мы дошли до верхнй ячейки
                mode = "vert" #? меняем на vert
                posY += 1 #? Прыгаем на клетку вниз
                cntY = row - 1  #? Обновляем счётчик с учётом прыжка
            else:
                posX += 1 #? Прыгаем на клетку вправо
                posY -= 1 #? Прыгаем на клетку наверх

    printTable(table)


if __name__ == "__main__":
    Program()