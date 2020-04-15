import sys
input = sys.stdin.readline

def getSum(mid):
    sum_ = 0
    for t in H:
        if t - mid > 0: sum_ += t - mid
    return sum_

def getMid(min_, max_):
    return (max_ + min_) // 2

def main(max_, min_, M):
    while True:
        mid = getMid(min_, max_)
        flag = getSum(mid)
        if flag < M: max_ = mid
        else:
            if max_ - mid <= 1: return mid, max_
            else: min_ = mid


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    H = list(map(int, input().strip().split()))
    max_, min_ = max(H), 0
    mid, max_ = main(max_, min_, M)
    if getSum(max_) >= M: print(max_)
    else: print(mid)