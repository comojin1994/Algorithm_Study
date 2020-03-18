import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().strip().split()))
    dp = [0 for _ in range(N)]
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print(max(dp))

'''
6
10 20 10 30 20 50

6
5 4 3 1 2 3
'''