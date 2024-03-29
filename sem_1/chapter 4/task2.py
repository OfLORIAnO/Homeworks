from itertools import permutations

def getVariants(m: list[int]) -> list[list[int]]:
    uniqVariants: set[tuple[int, ...]] = set()
    for elem in permutations(m):
        uniqVariants.add(tuple(elem))
    return list(map(lambda x: list(x), uniqVariants))

if __name__ == "__main__":
    print(getVariants([1, 1, 3]))
