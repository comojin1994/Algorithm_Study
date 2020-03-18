import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().strip().split()))
    dp1 = [0 for _ in range(N)]
    dp2 = [0 for _ in range(N)]
    max_ = 0

    for i in range(N):
        dp1[i] = 1
        i_ = N - i - 1
        dp2[i_] = 1
        for j in range(i):
            j_ = N - j - 1
            if nums[i] > nums[j] and dp1[i] < dp1[j] + 1:
                dp1[i] = dp1[j] + 1
            if nums[i_] > nums[j_] and dp2[i_] < dp2[j_] + 1:
                dp2[i_] = dp2[j_] + 1

    for i in range(N):
        if max_ < dp1[i] + dp2[i]: max_ = dp1[i] + dp2[i]
    print(max_-1)