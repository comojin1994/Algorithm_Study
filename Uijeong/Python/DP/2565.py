import sys
input = sys.stdin.readline


def LIS():
    for i in range(1, n):
        for j in range(i):
            if L[j] < L[i] != 0:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


def binary_search(arr, key):
    lower = 0
    upper = len(arr) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if key <= arr[mid]:
            upper = mid - 1
        else:
            lower = mid + 1
    return lower


def binary_LIS():
    lis_list = [L[0][1]]
    for i in range(1, n):
        if lis_list[-1] < L[i][1]:
            lis_list.append(L[i][1])
        else:
            idx = binary_search(lis_list, L[i][1])
            lis_list[idx] = L[i][1]
    return len(lis_list)


if __name__ == "__main__":
    n = int(input())
    # dp = [0] * 500
    # L = [0] * 500
    # for _ in range(n):
    #     i, j = map(int, input().split())
    #     dp[i-1] = 1
    #     L[i-1] = j
    L = [list(map(int, input().split())) for _ in range(n)]
    L = sorted(L, key=lambda x: x[0])

    print(n - binary_LIS())