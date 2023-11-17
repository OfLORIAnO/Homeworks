def copyElemInNewArray(array):
    newArr = []
    for e in array:
        newArr.append(e)
    return newArr


def deleteFromArray(array, leftInd, rigthInd):
    newArr = array
    for i in range(len(array)):
        if i == leftInd:
            newArr[i] = ""
        elif i == rigthInd:
            newArr[i] = ""
    return newArr


def getPair(lElem, rElem):
    coop = ["()", "{}", "[]"]
    for el in coop:
        if el[0] == lElem and el[1] == rElem:
            return True


def convertStringToArray(str):
    mass = []
    for elem in str:
        mass.append(elem)
    return mass


def isEmpty(array):
    cnt = 0
    for i in range(len(array)):
        if array[i] == "":
            cnt += 1
    return cnt == len(array)


def checkUncorrect(array, mass):
    newMass = [" "] * (len(mass) + 1)
    for i in range(len(array)):
        if array[i] == "":
            newMass[i] = mass[i]
        else:
            newMass[i] = " "
    newMass = "".join(newMass).split()
    tempString = ""
    for elem in newMass:
        if len(elem) >= len(tempString):
            tempString = elem
    if len(tempString) > 0:
        return tempString
    else:
        return False


def bracket(s): #! Основная функция
    mass = convertStringToArray(s)
    l, r, flag = 0, 1, False
    newArr = copyElemInNewArray(mass)
    while not (isEmpty(newArr)):  # ? Пока в списке есть скобки
        lElem = newArr[l]
        rElem = newArr[r]
        if getPair(lElem, rElem):  # ? Если есть пара
            newArr = deleteFromArray(newArr, l, r)
            flag = True
        elif rElem == "":  # ? Если правый символ пустой, то двинуться вправо
            r += 1
            if r >= len(newArr):  # ? Если выходим за границы списка
                l, r = 0, 1  # ? Начинаем сначала
                if flag == False:  # ? Если не было ни одной пары в списке
                    return checkUncorrect(newArr, mass)
                flag = False
            continue
        else:  # ? Иначе двигаемся вперёд
            l += 1
            r = l + 1
        if l >= len(newArr) or r >= len(newArr) - 1:  # ? Если дошли до конца списка
            l, r = 0, 1  # ? начинаем сначала
            if flag == False:  # ? Если не было ни одной пары в списке
                return checkUncorrect(newArr, mass)
            flag = False
    return True


if __name__ == "__main__":
    print("1 ", bracket("{}{}{}{[{}()][()[]][()()]}"))  #! True
    print("2 ", bracket("{{{{}}}{{{}}}}}"))  #! False {{{{}}}{{{}}}}
    print("3 ", bracket("{}()[{}]"))  #! True
    print("4 ", bracket("{}[][][]()()()({)(})[{}]"))  #! False {}[][][]()()()
    print("5 ", bracket("{[(]){[()]}}"))  #! False {[()]}
    print("6 ", bracket("())(())))"))  #! False (())
    print("7 ", bracket("}{)("))  #! False
