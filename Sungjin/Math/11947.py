import sys
input = sys.stdin.readline

def func(N, len_):
    temp = int('4' + '9' * (len_-1))
    if N < temp:
        return (int('9'*len_) - N) * N
    else:
        return (int('9'*len_) - temp) * temp

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = input().strip()
        len_ = len(N)
        N = int(N)
        print(func(N, len_))