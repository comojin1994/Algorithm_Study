import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    val = list(map(int, input().strip().split()))
    dp = [0] * N
    dp[0] = val[0]
    for i in range(1, N):
        dp[i] = max(dp[i-1] + val[i], val[i])
    print(max(dp))