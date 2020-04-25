import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    val = [int(input()) for _ in range(n)]
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(val[i], k + 1):
            dp[j] += dp[j - val[i]]
    print(dp[k])