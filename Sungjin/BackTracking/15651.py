import sys
input = sys.stdin.readline

def func(index, N, M):
    if index == M:
        print(' '.join(map(str,result)))
        return 1

    for n in nums:
        check[n-1] = True
        result[index] = n
        func(index+1, N, M)
        check[n-1] = False

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    nums = [i+1 for i in range(N)]
    check = [False for _ in range(N)]
    result = [0 for _ in range(M)]
    index = 0
    func(index, N, M)