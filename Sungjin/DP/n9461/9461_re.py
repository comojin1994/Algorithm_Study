import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        if N in [1, 2, 3]: print(1)
        else:
            dp = [0] * N
            dp[0], dp[1], dp[2] = 1, 1, 1
            for i in range(3, N):
                dp[i] = dp[i-2] + dp[i-3]
            print(dp[-1])