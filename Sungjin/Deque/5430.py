import sys
input = sys.stdin.readline

def Rev(s, e, cnt):
    temp = s
    s = e
    e = temp
    cnt += 1
    return s, e, cnt

def Del(s, e, ecnt):
    if s == e:
        ecnt += 1
        return s, e, ecnt

    if s < e:
        s += 1
    elif s > e:
        s -= 1
    return s, e, ecnt

def do(fuc, n):
    s, e = 0, n
    cnt, ecnt = 0, 0
    for f in fuc:
        if f == 'R':
            s, e, cnt = Rev(s, e, cnt)
        elif f == 'D':
            s, e, ecnt = Del(s, e, ecnt)
        if ecnt == 1:
            return s, e, cnt, ecnt

    return s, e, cnt, ecnt

def print_(s, e, cnt, ecnt, nums):
    if ecnt == 1:
        print('error')
        return 1

    if s == e:
        print('[]')
        return 1

    if cnt % 2 == 0:
        print('[', end='')
        for i in range(s, e-1):
            print('%s,' % nums[i], end='')
        print('%s]' % nums[e-1])
    else:
        print('[', end='')
        for i in range(s-1, e, -1):
            print('%s,' % nums[i], end='')
        print('%s]' % nums[e])
    return 1

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        fuc = input().strip()
        n = int(input())
        nums = input().strip()[1:-1].split(',')
        s, e, cnt, ecnt = do(fuc, n)
        print_(s, e, cnt, ecnt, nums)