def copyElemInNewArray(array):
    newArr = []
    for e in array:
        newArr.append(e)
    return newArr


def deleteFromArray(array, leftInd, rigthInd):
    newArr = []
    for i in range(len(array)):
        if i != leftInd and i != rigthInd:
            newArr.append(array[i])
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


def skob(s):
    mass = convertStringToArray(s)
    l = 0
    r = l + 1
    newArr = copyElemInNewArray(mass)
    flag = False
    while len(newArr) > 0:
        lElem = newArr[l]
        rElem = newArr[r]
        if getPair(lElem, rElem):
            newArr = deleteFromArray(newArr, l, r)
            flag = True
        l += 1
        r = l + 1
        if l >= (len(newArr) - 2) or len(newArr) == 2:
            l = 0
            r = l + 1
            if flag == False:
                return False
            flag = False
    return True


if __name__ == "__main__":
    print(skob("{}()[{}]"))
    print(skob("{}[][][]()()()()()[{}]"))
    print(skob("{[(]){[()]}}"))
