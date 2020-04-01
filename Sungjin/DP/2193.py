import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    dp = [0] * (N + 1)
    dp[0:4] = [1, 1, 1, 2]
    for i in range(4, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N])