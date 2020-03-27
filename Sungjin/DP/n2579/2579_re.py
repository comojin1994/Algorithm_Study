import sys
input = sys.stdin.readline

def init_dp(n, stair):
    dp = [0] * n
    dp[0] = stair[0]
    dp[1] = sum(stair[:2])
    dp[2] = max(stair[0], stair[1]) + stair[2]
    return dp

if __name__ == '__main__':
    n = int(input())
    stair = [int(input()) for _ in range(n)]
    if n == 1: print(stair[0])
    elif n == 2: print(sum(stair[:2]))
    elif n == 3: print(max(stair[0], stair[1]) + stair[2])
    else:
        dp = init_dp(n, stair)
        for i in range(3, n):
            dp[i] = max(dp[i-2], stair[i-1] + dp[i-3]) + stair[i]
        print(dp[-1])