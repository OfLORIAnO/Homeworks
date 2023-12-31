def checkPair(a: list[str]) -> list[list[str]]:
    d: dict[str, list[str]] = dict()
    for elem in a:
        d.setdefault("".join(sorted(elem)), list()).append(elem)
    return list(d.values())


if __name__ == "__main__":
    a = [
        "wqe",
        "qwe",
        "ewq",
        "dsa",
        "dsas",
        "asd",
        "qwee",
        "zxc",
        "cxz",
        "xxz",
        "z",
        "s",
        "qweasdzxc",
        "zzxc",
    ]
    print(checkPair(a))
