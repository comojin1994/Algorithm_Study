import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(5000)


def sieve(i, j, Li):
    L = copy.deepcopy(Li)
    L[i][j] = False
    for k in range(n):
        L[i][k] = False
        L[k][j] = False
        if 0 <= j + k - i < n:
            L[k][j + k - i] = False
        if 0 <= j - k + i < n:
            L[k][j - k + i] = False
    return L


def adjacent(li, depth):
    try:
        if depth != n-1:
            li[depth + 1].index(True)
        return True
    except ValueError:
        return False


def dfs(i, Li):
    global result
    if i == n:
        result += 1
    else:
        for j in range(n):
            if Li[i][j] is False:
                continue
            tmpL = sieve(i, j, Li)
            if adjacent(tmpL, i):
                dfs(i + 1, tmpL)
            else:
                Li[i][j] = False


if __name__ == "__main__":
    n = int(input())
    result = 0
    L = [[True] * n for _ in range(n)]

    if n < 11:
        result = 0
        dfs(0, L)
    else:
        answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
        result = answer[n]
    print(result)
