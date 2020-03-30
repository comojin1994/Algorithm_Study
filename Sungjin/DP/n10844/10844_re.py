import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    fix = 10**9
    dp = [[0] * 12 for _ in range(N)]
    dp[0] = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    for i in range(1, N):
        for j in range(1, 11):
            dp[i][j] = (dp[i-1][j-1] % fix) + (dp[i-1][j+1] % fix)
    print(sum(dp[-1]) % fix)