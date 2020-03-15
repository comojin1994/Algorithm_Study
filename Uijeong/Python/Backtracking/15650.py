import sys

input = sys.stdin.readline


def dfs(x, l):
    global L, finalL
    if x == m:
        if L not in finalL:
            finalL.append(L)
    else:
        for i in range(l, n+1):
            L = L[:x]
            if i in L:
                continue
            else:
                L.append(i)
                dfs(x+1, i)


if __name__ == "__main__":
    n, m = map(int, input().split())
    L, finalL = [], []
    dfs(0, 1)

    for li in finalL:
        for i in li:
            print(i, end=" ")
        print()