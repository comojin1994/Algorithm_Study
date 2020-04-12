import sys
input = sys.stdin.readline

def isAll(idx, jdx, N):
    seed = paper[idx][jdx]
    for i in range(N):
        for j in range(N):
            if paper[idx + i][jdx + j] != seed: return False
    return True

def check(idx, jdx, N):
    if isAll(idx, jdx, N):
        result[paper[idx][jdx] + 1] += 1
    else:
        for i in range(3):
            for j in range(3):
                check(idx + i * (N // 3), jdx + j * (N // 3), N // 3)

if __name__ == '__main__':
    N = int(input())
    paper = [list(map(int, input().strip().split())) for _ in range(N)]
    result = [0, 0, 0]
    check(0, 0, N)
    for r in result:
        print(r)