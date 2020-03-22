import sys

input = sys.stdin.readline


def LIS(A):
    global dp
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def binary_search(arr, n):
    lower = 0
    upper = len(arr) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if n <= arr[mid]:
            upper = mid - 1
        else:
            lower = mid + 1
    return lower


def bs_LIS(arr):
    lis_list = [arr[0]]
    for i in range(1, len(arr)):
        if lis_list[-1] < arr[i]:
            lis_list.append(arr[i])
        else:
            idx = binary_search(lis_list, arr[i])
            lis_list[idx] = arr[i]
    return lis_list


if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    print(LIS(A))
