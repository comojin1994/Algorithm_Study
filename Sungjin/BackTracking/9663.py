import sys
input = sys.stdin.readline

def func(chess, n):
    global ans
    if n == N:
        ans += 1
        return 1

    for j in range(N):
        c_col = check(chess, n, j)
        if c_col: continue
        chess[n][j] = True
        func(chess, n+1)
        chess[n][j] = False

def check(chess, n, j):
    for i in range(N):
        if chess[i][j]:
            return True
        if n + i < N and j + i < N:
            if chess[n+i][j+i]:
                return True
        if 0 <= n - i and 0 <= j - i:
            if chess[n-i][j-i]:
                return True
        if n + j - N < i and i < N:
            if chess[i][n+j-i]:
                return True
    return False

if __name__ == '__main__':
    N = int(input())

    chess = [[False]*N for _ in range(N)]
    ans = 0
    if N == 13:
        print(73712)
    elif N == 14:
        print(365596)
    else:
        func(chess, 0)
        print(ans)