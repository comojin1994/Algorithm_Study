import sys
input = sys.stdin.readline

if __name__ == '__main__':
    L = int(input())
    S = list(input().strip())
    M = 1234567891
    sum_ = 0
    for idx, s in enumerate(S):
        t = ord(s) - 96
        sum_ += t * (31 ** idx)
    print(sum_ % M)