def delete(n):
    tempL = list(map(int, str(n)))
    return n + sum(tempL)


def recursive(n, recL):
    n = delete(n)
    # print(n)
    if n > 10000 or n in recL:
        recL.sort()
        return recL
    recL.append(n)
    recursive(n, recL)


if __name__ == "__main__":
    L = []
    for i in range(1, 10001):
        if i in L:
            continue
        tempL = recursive(i, L)
        if tempL:
            L = list(set(tempL))

    for i in range(1, 10001):
        if i not in L:
            print(i)
