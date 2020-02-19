import sys

input = sys.stdin.readline


def bisect(nums, n, lo, hi):
    if n > nums[-1]:
        return False
    if lo > hi:
        return False

    mid = (hi + lo) // 2
    if nums[mid] == n:
        return True
    elif nums[mid] > n:
        return bisect(nums, n, lo, mid - 1)
    else:
        return bisect(nums, n, mid + 1, hi)


if __name__ == '__main__':
    N = int(input())
    nums = sorted(list(map(int, input().strip().split())))
    M = int(input())
    test = list(map(int, input().strip().split()))
    for n in test:
        if bisect(nums, n, 0, N - 1):
            print(1)
        else:
            print(0)