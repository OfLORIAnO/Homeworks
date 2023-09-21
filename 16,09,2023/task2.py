def reverseWords(s):
    tempString = ""
    l = 0
    for i in range(0, len(s)):
        if s[i] == " ":
            tempString = s[l:i] + " " + tempString
            l = i + 1
        if i == len(s) - 1:
            tempString = s[l : len(s)] + " " + tempString
    return tempString


def deleteSpaces(s):
    tempString = ""

    for i in range(len(s) - 1):
        if s[i] == " " and s[i + 1] == " ":
            continue
        else:
            tempString = tempString + s[i]
    return tempString


def convert(s):
    return  deleteSpaces(reverseWords(s.strip().lower())).capitalize()


if __name__ == "__main__":
    print(convert("      мИр приВет        "))
    print(convert("      мИр приВет страус      "))
    print(convert("      it    was     cool      "))
    print(convert("good"))
