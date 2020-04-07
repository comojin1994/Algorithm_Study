import sys
input = sys.stdin.readline

def get_cnt(n, num):
    cnt = 0; i = 1
    while num**i <= n:
        cnt += n // num**i
        i += 1
    return cnt

def cal(n ,m, num):
    return get_cnt(n, num) - (get_cnt(m, num) + get_cnt(n-m, num))

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    print(min(cal(n, m, 5), cal(n, m, 2)))