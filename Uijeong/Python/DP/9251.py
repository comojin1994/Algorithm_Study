import sys
input = sys.stdin.readline


def LCS():
    global lcs
    for i in range(1, n):
        for j in range(1, m):
            if A[j-1] == B[i-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    return lcs[n - 1][m - 1]


if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    m, n = len(A) + 1, len(B) + 1
    lcs = [[0] * m for _ in range(n)]
    print(LCS())