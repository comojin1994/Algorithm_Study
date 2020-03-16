import sys

input = sys.stdin.readline


def dfs(x, l):
    global L
    if x == m:
        for li in L:
            print(li, end=' ')
        print()
    else:
        for i in range(l, n+1):
            L = L[:x]
            L.append(i)
            dfs(x+1, i)


if __name__ == "__main__":
    n, m = map(int, input().split())
    L = []
    dfs(0, 1)