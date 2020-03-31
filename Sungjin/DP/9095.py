import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    dp = [0] * 11
    dp[:4] = [1, 1, 2, 4]
    for i in range(4, 11):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    for _ in range(T):
        n = int(input())
        print(dp[n])