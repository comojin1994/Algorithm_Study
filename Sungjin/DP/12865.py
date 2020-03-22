import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    thing = [list(map(int, input().strip().split())) for _ in range(N)]
    dp = [[0] * (K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            if j < thing[i-1][0]:
                dp[i][j] = max(0, dp[i-1][j])
            else:
                dp[i][j] = max(dp[i - 1][j], thing[i - 1][1] + dp[i - 1][j - thing[i - 1][0]])
    print(dp[N][-1])


'''
4 2
1 1
5 1
5 1
1 1
'''