def generator():
    last = n - 10**(len(str(n))-1)
    L = []
    for i in range(n, last, -1):
        tmpL = list(map(int, str(i)))
        if n == i + sum(tmpL):
            L.append(i)
    return min(L) if len(L) != 0 else 0


if __name__ == "__main__":
    n = int(input())
    k = n // 10**(len(str(n))-1)
    print(generator())