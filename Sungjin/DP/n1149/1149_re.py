import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    paint = [list(map(int, input().strip().split())) for _ in range(N)]
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = paint[0]
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + paint[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + paint[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + paint[i][2]
    print(min(dp[-1]))