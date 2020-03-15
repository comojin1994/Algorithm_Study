import sys

input = sys.stdin.readline


def dfs(x):
    global L
    if x == m:  # break point
        for li in L:
            print(li, end=" ")
        print()
    else:
        for i in range(1, n+1):
            L = L[:x]
            if i in L:
                continue
            else:
                L.append(i)
                dfs(x+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    L = []
    dfs(0)