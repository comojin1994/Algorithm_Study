import sys
input = sys.stdin.readline

def func(idx, result):
    if idx == M:
        print(' '.join(map(str, result)))
        return 1

    for i in range(N):
        check[i] = True
        result[idx] = nums[i]
        func(idx + 1, result)
        result[idx] = 0
        check[i] = False

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    nums = sorted(list(map(int, input().strip().split())))
    check = [False] * N
    result = [0] * M
    func(0, result)