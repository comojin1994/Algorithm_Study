import sys
import copy
input = sys.stdin.readline


def triangle():
    Line = L[0] + [0] * (n-1)
    for i in range(1, n):
        tmp = copy.deepcopy(Line)
        for j in range(1, i):
            Line[j] = max(tmp[j-1], tmp[j]) + L[i][j]
        Line[0] = L[i][0] + tmp[0]
        Line[i] = L[i][-1] + tmp[i-1]
    return max(Line)


if __name__ == "__main__":
    n = int(input())
    L = [list(map(int, input().split())) for _ in range(n)]
    print(triangle())