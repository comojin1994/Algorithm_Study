import sys
input = sys.stdin.readline

def bisect(nums, x, lo, hi):
    if x > nums[-1]:
        return False
    if lo > hi:
        return False
    mid = (hi + lo) // 2
    if nums[mid] == x:
        return True
    elif nums[mid] < x:
        return bisect(nums, x, mid + 1, hi)
    else:
        return bisect(nums, x, lo, mid - 1)

if __name__ == '__main__':
    N = int(input())
    nums = sorted(list(map(int, input().strip().split())))
    M = int(input())
    test = list(map(int, input().strip().split()))

    for n in test:
        if bisect(nums, n, 0, N-1):
            print(1)
        else:
            print(0)