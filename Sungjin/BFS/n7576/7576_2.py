import sys
input = sys.stdin.readline

def checkMinus():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0: return True
    return False

def checkZero(i, j):
    L = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]
    result = []
    for li in L:
        if li[0] < 0 or li[1] < 0 or li[0] > N - 1 or li[1] > M - 1: continue
        if graph[li[0]][li[1]] == 0:
            result.append([li[0], li[1]])
            graph[li[0]][li[1]] = 1
    return result

def BFS(check, cnt):
    visited = []
    for c in check:
        visited += checkZero(c[0], c[1])
    return visited

def main(check):
    cnt = 0
    while check:
        check = BFS(check, cnt)
        cnt += 1
    if cnt == 0: return 0
    else: return cnt - 1

if __name__ == '__main__':
    M, N = map(int, input().strip().split())
    graph = [list(map(int, input().strip().split())) for _ in range(N)]
    check = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1: check.append([i, j])
    result = main(check)
    if checkMinus(): print(-1)
    else: print(result)