def endNumber():
    L = []
    for k in range(lenN + 1):
        for i in range(10**(lenN-k)):
            for j in range(10**k):
                L.append(int(str(i) + '666' + str(j)))
            L.append(int(str(i) + '666'))
    L = list(set(L))
    L.sort()
    return L[int(n)-1]


if __name__ == "__main__":
    # n = input()
    # lenN = len(n)
    for n in range(100):
        lenN = len(str(n))
        print(endNumber())