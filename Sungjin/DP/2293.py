import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    val = [int(input()) for _ in range(n)]
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for idx, v in enumerate(val):
        dp[v][idx] = 1
    for i in range(1, k + 1):
        for j in range(n-1, -1, -1):
            dp[i][j] += dp[i - val[j]][j] + dp[i][j+1] if i - val[j] >= 0 else dp[i][j+1]
    print(dp[-1][0])