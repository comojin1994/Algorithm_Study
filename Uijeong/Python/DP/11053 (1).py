import sys
input = sys.stdin.readline


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
    lis_list = [L[1]]
    for i in range(2, 501):
        if L[i] == 0:
            continue
        elif lis_list[-1] < L[i]:
            lis_list.append(L[i])
        else:
            idx = binary_search(lis_list, L[i])
            lis_list[idx] = L[i]
            lis_list = lis_list[:idx+1]
    return len(lis_list)


if __name__ == "__main__":
    n = int(input())
    dp = [0] * 501
    L = [0] * 501
    for _ in range(n):
        i, j = map(int, input().split())
        dp[i] = 1
        L[i] = j
    print(n - binary_LIS())