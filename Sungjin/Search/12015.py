import sys
input = sys.stdin.readline

def getMid(min_, max_):
    return (min_ + max_) // 2

def getLower(n):
    min_, max_ = 0, len(result) - 1
    mid = getMid(min_, max_)
    while min_ <= max_:
        mid = getMid(min_, max_)
        if n > result[mid]:
            min_ = mid + 1
        else:
            max_ = mid - 1
    return mid

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().strip().split()))
    result = [nums[0]]
    for n in nums:
        if n > result[-1]: result.append(n)
        else:
            idx = getLower(n)
            if result[idx] < n: result[idx + 1] = n
            else: result[idx] = n
    print(len(result))