import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M, K = map(int, input().strip().split())
    dp = [M + 1] * N
    for i in range(N):
        temp = list(map(int, input().strip().split()))
        check = 0
        for idx, t in enumerate(temp):
            check += t
            if check >= K:
                dp[i] = idx + 1
                break
    print(dp.index(min(dp)) + 1, min(dp))