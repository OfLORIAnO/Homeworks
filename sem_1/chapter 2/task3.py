from typing import Union


def copyElemInNewArray(array: list[str]) -> list[str]:
    newArr: list[str] = []
    for e in array:
        newArr.append(e)
    return newArr


def deleteFromArray(array: list[str], leftInd: int, rigthInd: int):
    newArr: list[str] = array
    for i in range(len(array)):
        if i == leftInd:
            newArr[i] = ""
        elif i == rigthInd:
            newArr[i] = ""
    return newArr


def getPair(lElem: str, rElem: str) -> bool:
    coop: list[str] = ["()", "{}", "[]"]
    for el in coop:
        if el[0] == lElem and el[1] == rElem:
            return True
    return False


def convertStringToArray(string: str) -> list[str]:
    mass: list[str] = []
    for elem in string:
        mass.append(elem)
    return mass


def isEmpty(array: list[str]) -> bool:
    cnt = 0
    for i in range(len(array)):
        if array[i] == "":
            cnt += 1
    return cnt == len(array)


def checkUncorrect(array: list[str], mass: list[str]) -> Union[str, bool]:
    newMass: list[str] = [" "] * (len(mass) + 1)
    for i in range(len(array)):
        if array[i] == "":
            newMass[i] = mass[i]
        else:
            newMass[i] = " "
    newMass = "".join(newMass).split()
    tempString: str = ""
    for elem in newMass:
        if len(elem) >= len(tempString):
            tempString = elem
    if len(tempString) > 0:
        return tempString
    else:
        return False


def bracket(s: str):  #! Основная функция
    mass: list[str] = convertStringToArray(s)
    l: int = 0
    r: int = 1
    flag: bool = False
    newArr: list[str] = copyElemInNewArray(mass)
    while not (isEmpty(newArr)):  # ? Пока в списке есть скобки
        lElem: str = newArr[l]
        rElem: str = newArr[r]
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
