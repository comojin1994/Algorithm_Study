import sys

input = sys.stdin.readline


def resident():
    L = []

    # first floor
    tempL = [m + 1 for m in range(n)]
    L.append(tempL)

    # start from second floor
    for i in range(k):
        tempL = [1]
        for j in range(1, n):
            tempL.append(tempL[j - 1] + L[i][j])
        L.append(tempL)
    return L[k][n - 1]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        n = int(input())
        print(resident())

