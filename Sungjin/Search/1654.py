import sys
input = sys.stdin.readline

def get_binary(min_, max_):
    return (min_ + max_) // 2

def get_sum(mid):
    result = 0
    for l in lan:
        result += l // mid
    return result

def get_min(min_, max_):
    while True:
        mid = get_binary(min_, max_)
        flag = get_sum(mid)
        if flag >= N:
            min_ = mid
            if max_ - mid <= 1: break
        else: max_ = mid
    if get_sum(max_) == N: return max_
    else: return mid

if __name__ == '__main__':
    K, N = map(int, input().strip().split())
    lan = [int(input()) for _ in range(K)]
    min_ = 1
    max_ = max(lan)
    result = 0
    print(get_min(min_, max_))