import sys
from itertools import combinations
input = sys.stdin.readline


def dfs(x, k):
    global minAbs
    if x == n//2:
        startSc, linkSc = 0, 0
        link = list(set(space) - set(start))
        for i, j in combinations(start, 2):
            startSc += addL[i][j]
        for i, j in combinations(link, 2):
            linkSc += addL[i][j]
        if minAbs > abs(startSc - linkSc):
            minAbs = abs(startSc - linkSc)
        return
    for j in range(k, n):
        start.append(j)
        dfs(x+1, j+1)
        start.pop(-1)


if __name__ == "__main__":
    n = int(input())
    L = [list(map(int, input().split())) for _ in range(n)]
    addL = [[0]*n for _ in range(n)]
    space = [i for i in range(n)]
    start, link, minAbs = [], [], 1000
    for i in range(n):
        for j in range(i+1, n):
            addL[i][j] = L[i][j] + L[j][i]
    dfs(0, 0)
    print(minAbs)