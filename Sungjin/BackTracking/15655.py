import sys
input = sys.stdin.readline

def func(idx, j):
    if idx == M:
        print(' '.join(map(str, result)))
        return 1

    for i, n in enumerate(nums):
        if i >= j:
            if check[i]: continue

            check[i] = True
            result[idx] = n
            func(idx+1, i)
            check[i] = False
            result[idx] = n

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    nums = sorted(nums)
    result = [0 for _ in range(M)]
    check = [False for _ in range(N)]
    func(0, 0)