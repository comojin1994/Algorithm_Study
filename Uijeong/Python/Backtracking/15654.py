import sys
input = sys.stdin.readline


def dfs(x):
    if x == m:  # base case
        print(' '.join(map(str, L)))
        return
    else:
        for li in arr:
            if li not in L:
                L.append(li)
                dfs(x+1)
                L.remove(li)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    L = []
    dfs(0)