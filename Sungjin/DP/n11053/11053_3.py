import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().strip().split()))
    dp = [0 for _ in range(1001)]
    for i in range(N):
        dp[nums[i]] = max(dp[:nums[i]]) + 1
    print(max(dp))