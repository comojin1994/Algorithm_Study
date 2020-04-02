import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    pi = [0] + list(map(int, input().strip().split()))
    dp = [0] * (N+1)
    dp[1] = pi[1]

    for i in range(2, N+1):
        max_ = 0
        for j in range(1, i+1):
            temp = dp[i - j] + pi[j]
            if max_ < temp: max_ = temp
        dp[i] = max_
    print(dp[-1])