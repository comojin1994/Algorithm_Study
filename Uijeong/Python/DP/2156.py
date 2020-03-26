import sys
import copy
input = sys.stdin.readline


def drink():
    Fi_2, Fi_1 = [0, 0], [L[0], 0]
    maxFi_2 = 0
    for i in range(1, n):
        maxFi_2 = max(max(Fi_2), maxFi_2)
        Fi_2 = copy.deepcopy(Fi_1)
        Fi_1 = [maxFi_2 + L[i], Fi_1[0] + L[i]]
    return max(Fi_1 + Fi_2)


if __name__ == "__main__":
    n = int(input())
    L = [int(input()) for _ in range(n)]
    print(drink())