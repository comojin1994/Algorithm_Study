import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    L = [list(map(int, input().strip().split())) for _ in range(n)]
    L = sorted(L, key=lambda x: [x[1], x[0]])
    for [x, y] in L:
        print(x, y)