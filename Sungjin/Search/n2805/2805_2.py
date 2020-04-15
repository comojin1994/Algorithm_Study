import sys
from collections import Counter
input = sys.stdin.readline

def getSum(mid):
    sum_ = 0
    for t in H:
        if t - mid > 0: sum_ += t - mid
    return sum_

def getMid(min_, max_):
    return (max_ + min_) // 2

def main(max_, min_, M):
    ans = 0
    while min_ <= max_:
        mid = getMid(min_, max_)
        flag = getSum(mid)
        if flag < M: max_ = mid - 1
        else: min_ = mid + 1; ans = mid
    return ans

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    H = list(map(int, input().strip().split()))
    max_ = max(Counter(H).keys())
    min_ = max_ - M if max_ > M else 0
    print(main(max_, min_, M))