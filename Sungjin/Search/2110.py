import sys
input = sys.stdin.readline

def getMid(min_, max_):
    return (min_ + max_) // 2

def checkCnt(n):
    start = H[0]
    cnt = 1
    for h in H:
        if h >= start + n:
            cnt += 1
            start = h
            # print('h', h)
    # print('cnt', cnt, 'n', n)
    return cnt

if __name__ == '__main__':
    N, C = map(int, input().strip().split())
    H = sorted([int(input()) for _ in range(N)])
    min_, max_ = 1, H[-1] - H[0]
    while min_ <= max_:
        mid = getMid(min_, max_)
        cnt = checkCnt(mid)
        if mid - min_ <= 1 or max_ - mid <= 1: break

        if cnt > C:
            min_ = mid - 1
        elif cnt <= C:
            max_ = mid + 1
        # print(min_, mid, max_)
    for n in range(max_, mid - 1, -1):
        if checkCnt(n) >= C: print(n); break