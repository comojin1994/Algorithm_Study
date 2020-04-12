# pypy 통과
import sys
input = sys.stdin.readline

def get_new(paper, x, y):
    result = []
    for i in range(x[0], y[0]):
        result.append(paper[i][x[1]:y[1]])
    return result

def isAll(paper, N):
    start = paper[0][0]
    for i in range(N):
        for j in range(N):
            if paper[i][j] != start: return False
    return True

def check(paper, N):
    global result
    tf = isAll(paper, N)
    if tf:
        result[paper[0][0]] += 1
    else:
        for i in range(0, N, N // 3):
            for j in range(0, N, N // 3):
                check(get_new(paper, (i, j), (i + N // 3, j + N // 3)), N // 3)

if __name__ == '__main__':
    N = int(input())
    paper = [list(map(int, input().strip().split())) for _ in range(N)]
    result = {-1: 0, 0: 0, 1: 0}
    check(paper, N)
    for _, v in sorted(list(result.items()), key=lambda x: x[0]):
        print(v)