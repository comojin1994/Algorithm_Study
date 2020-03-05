import sys

input = sys.stdin.readline


def square(d):
    for i in range(n-d):
        for j in range(m-d):
            if L[i][j] == L[i+d][j+d] == L[i][j+d] == L[i+d][j]:
                return True
    return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    L = [list(map(int, input().strip())) for _ in range(n)]

    maxD = 0
    for d in range(0, n):
        if square(d):
            maxD = (d+1)**2

    print(maxD)