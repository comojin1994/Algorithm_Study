import sys
import math
input = sys.stdin.readline


if __name__ == "__main__":
    n, k = map(int, input().split())
    k = min(n-k, k)
    L = [[1] * (n+1)] + [[0] * (n+1) for _ in range(k)]
    for i in range(1, k+1):
        for j in range(i, n+1):
            L[i][j] = (L[i-1][j-1] + L[i][j-1]) % 10007 if i != j else 1
    print(L[k][n])