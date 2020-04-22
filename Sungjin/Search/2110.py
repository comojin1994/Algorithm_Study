import sys
input = sys.stdin.readline

def getMid(min_, max_):
    return (min_ + max_) // 2

def checkCnt(mid):
    start, cnt = 0, 1
    for idx, h in enumerate(H):
        if H[start] + mid <= h:
            cnt += 1
            start = idx
    return cnt

if __name__ == '__main__':
    N, C = map(int, input().strip().split())
    H = sorted([int(input()) for _ in range(N)])
    min_, max_ = 1, H[-1] - H[0]
    result = 0
    while min_ <= max_:
        mid = getMid(min_, max_)
        cnt= checkCnt(mid)
        if cnt < C: max_ = mid - 1
        else: min_ = mid + 1; result = mid
    print(result)

'''
4 3
999999985
999999991
999999996
1000000000

4 3
1
3
5
7
'''