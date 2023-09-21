def task1(s):
    listOfSubs = []
    charsWas = []
    tempString = ""
    for i in range(0, len(s)):
        char = s[i]
        if char not in charsWas:
            tempString += char
        else:
            listOfSubs.append(tempString)
            tempString = char
            charsWas = []
        charsWas.append(char)
    maxLenWord = ''
    for i in range(len(listOfSubs)):
        if len(maxLenWord) <= len(listOfSubs[i]):
            maxLenWord = listOfSubs[i]
    return maxLenWord


if __name__ == "__main__":
    print(task1("qweasdfdqw"))
    print(task1("aaaaaaaa"))
    print(task1("prrker"))
