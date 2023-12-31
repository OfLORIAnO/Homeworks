def task1() -> str:
    s: str = input()
    listOfSubs: list[str] = []
    charsWas: list[str] = []
    tempString: str = ""
    for i in range(0, len(s)):
        char: str = s[i]
        if char not in charsWas:
            tempString += char
        else:
            listOfSubs.append(tempString)
            tempString = char
            charsWas = []
        charsWas.append(char)
    maxLenWord = ""
    for i in range(len(listOfSubs)):
        if len(maxLenWord) <= len(listOfSubs[i]):
            maxLenWord = listOfSubs[i]
    print(maxLenWord)
    return maxLenWord


if __name__ == "__main__":
    task1()
