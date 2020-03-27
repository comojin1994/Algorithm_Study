import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    tri = [[0] + list(map(int, input().strip().split())) + [0] * (n - 1 - i) for i in range(n)]
    dp = [[0] * (n+1) for _ in range(n)]
    dp[0] = tri[0]
    for i in range(n):
        for j in range(1, i+2):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tri[i][j]
    print(max(dp[-1]))