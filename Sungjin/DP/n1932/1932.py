import sys
input = sys.stdin.readline

def func(idx):
    if idx == N-1:
        print(max(result[idx]))
        return 1

    for i, n in enumerate(tri[idx]):
        result[idx+1][i] = max(result[idx][i] + tri[idx+1][i], result[idx+1][i])
        result[idx+1][i+1] = max(result[idx][i] + tri[idx+1][i+1], result[idx+1][i+1])

    return func(idx+1)

if __name__ == '__main__':
    N = int(input())
    tri = [list(map(int, input().strip().split())) for _ in range(N)]
    result = [[0]*N for i in range(N)]
    result[0][0] = tri[0][0]
    func(0)