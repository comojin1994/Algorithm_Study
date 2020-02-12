import sys
input = sys.stdin.readline

def func(index, N, M):
    if index == M:
        print(' '.join(map(str,result)))
        return 1

    for i in range(N):
        if check[i]: continue
        check[i] = True
        result[index] = nums[i]
        func(index+1, N, M)
        check[i] = False

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    nums = [n for n in range(1,N+1)]
    check = [False for _ in range(10)]
    result = [0 for _ in range(M)]
    index = 0
    func(index, N, M)