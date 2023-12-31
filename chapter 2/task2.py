def reverseWords(s: str) -> str:
    tempString: str = ""
    l: int = 0
    for i in range(0, len(s)):
        if s[i] == " ":
            tempString = s[l:i] + " " + tempString
            l = i + 1
        if i == len(s) - 1:
            tempString = s[l : len(s)] + " " + tempString
    return tempString


def deleteSpaces(s: str) -> str:
    tempString: str = ""

    for i in range(len(s) - 1):
        if s[i] == " " and s[i + 1] == " ":
            continue
        else:
            tempString = tempString + s[i]
    print(tempString)
    return tempString


def convert() -> str:
    s: str = input()
    return deleteSpaces(reverseWords(s.strip().lower())).capitalize()


if __name__ == "__main__":
    convert()
