def generator():
    # 범위 지정으로 속도 최적화
    last = n - 9 * k + 1 if n > 9 * k + 1 else 0
    L = []
    for i in range(n, last, -1):
        sumL = 0
        for j in str(i):
            sumL += int(j)
        if n == i + sumL:
            L.append(i)
    return min(L) if len(L) != 0 else 0


if __name__ == "__main__":
    n = int(input())
    k = len(str(n))
    print(generator())