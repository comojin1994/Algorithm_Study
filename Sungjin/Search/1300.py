import sys
input = sys.stdin.readline

def getVal(N, mid):
    cnt = 0
    for i in range(1, N+1):
        val = mid // i
        if val >= N: cnt += N
        else: cnt += val
    return cnt

def getMid(min_, max_):
    return (min_ + max_) // 2

if __name__ == '__main__':
    N = int(input())
    k = int(input())
    min_, max_ = 0, min(10**9, N**2)
    result = 0
    while min_ <= max_:
        mid = getMid(min_, max_)
        val = getVal(N, mid)
        if val >= k: max_ = mid - 1; result = mid
        elif val < k: min_ = mid + 1
    print(result)