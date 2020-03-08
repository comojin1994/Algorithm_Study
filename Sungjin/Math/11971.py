import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    rule = [list(map(int, input().strip().split())) for _ in range(N)]
    yuen = [list(map(int, input().strip().split())) for _ in range(M)]
    result = [0 for _ in range(100)]
    init_ = 0
    for l, s in rule:
        for i in range(init_, init_ + l):
            result[i] = s
        init_ += l

    init_ = 0
    for l, s, in yuen:
        for i in range(init_, init_ + l):
            result[i] = s - result[i]
        init_ += l
    if max(result) < 0: print(0)
    else: print(max(result))