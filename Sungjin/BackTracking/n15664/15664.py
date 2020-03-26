import sys, copy
input = sys.stdin.readline

def func(idx, j, result):
    global out
    if idx == M:
        if result not in out:
            out.append(copy.deepcopy(result))
            print(' '.join(map(str, result)))
        return 1

    for i in range(j, N):
        if check[i]: continue
        check[i] = True
        result[idx] = nums[i]
        func(idx + 1, i, result)
        check[i] = False
        result[idx] = 0

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    nums = sorted(list(map(int, input().strip().split())))
    check = [False] * N
    result = [0] * M
    out = []
    func(0, 0, result)