import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    L = [list(map(int, input().strip().split())) for _ in range(n)]
    # lambda 에서 두가지 이상 비교하는 방법
    L = sorted(L, key=lambda x: [x[0], x[1]])
    for [x, y] in L:
        print(x, y)