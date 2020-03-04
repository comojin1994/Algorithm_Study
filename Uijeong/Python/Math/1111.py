import sys
import math

input = sys.stdin.readline


def IQ(x, y):
    for i in range(1, len(L)-1):
        if L[i + 1] != L[i] * x + y:
            return False
    return True


if __name__ == "__main__":
    N = int(input())
    L = list(map(int, input().split()))

    if N == 1:
        print("A")
        exit(0)
    elif N == 2:
        if L[0] == L[1]:
            print(L[0])
        else:
            print("A")
        exit(0)

    if 0 in L:
        if L[0] == L[1] == 0:
            k = 0
        else:
            k = 100
    else:
        k = math.fabs(L[1]//L[0])
    # 경우의 수 리스트
    prL = [(x, L[1] - L[0] * x) for x in range(-k, k+1)]
    nextL = [L[N-1] * x + y for x, y in prL if IQ(x, y)]

    if len(nextL) == 1:
        print(nextL[0])
    elif len(nextL) > 1:
        print("A")
    else:
        print("B")
