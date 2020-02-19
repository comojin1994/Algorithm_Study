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
    elif nums[mid] > x:
        return bisect(nums, x, lo, mid - 1)
    elif nums[mid] < x:
        return bisect(nums, x, mid + 1, hi)

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().strip().split()))
    dic = dict()
    for n in nums:
        if n in dic.keys(): dic[n] += 1
        else: dic[n] = 1
    nums_ = sorted(list(dic.keys()))
    M = int(input())
    test = list(map(int, input().strip().split()))
    for t in test:
        if bisect(nums_, t, 0, len(nums_) - 1):
            print(dic[t], end=' ')
        else: print(0, end=' ')