import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def func(N, i):
    if N == 0:
        return 0
    elif result[N][i] != 0:
        return result[N][i]

    result[N][i] = min([func(N-1, j) for j in range(3) if j != i]) + home[N-1][i]
    return result[N][i]

if __name__ == '__main__':
    N = int(input())
    home = [list(map(int, input().strip().split())) for _ in range(N)]
    result = [[0]*3 for _ in range(N+1)]
    for i in range(3):
        func(N, i)
    print(min(result[N]))