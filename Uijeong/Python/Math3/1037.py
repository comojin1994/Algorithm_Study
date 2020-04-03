import sys
import math
input = sys.stdin.readline


def divisor():
    global L
    if len(L) == 1:
        return L[0] ** 2
    else:
        return L[0] * L[-1]


if __name__ == "__main__":
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    print(divisor())