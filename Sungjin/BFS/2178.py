import sys
from collections import deque
input = sys.stdin.readline

def checkOne(i, j):
    L = [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]
    result = []
    for li in L:
        if li[0] < 0 or li[1] < 0 or li[0] > N - 1 or li[1] > M - 1: continue
        if graph[li[0]][li[1]] == 1: result.append([li[0], li[1]])
    return result

def BFS(i, j):
    que = deque([[i, j]])
    visited = []
    while que:
        n = que.popleft()
        li = checkOne(n[0], n[1])
        graph[n[0]][n[1]] = 0
        if n not in visited:
            for l in li:
                if l not in visited: que += [l]
            visited.append(n)
            if n == [N - 1, M - 1]: break
    return visited

def calcDist(i, result):
    if abs(result[-1][0] - path[i][0]) == 1 and result[-1][1] - path[i][1] == 0: return True
    elif result[-1][0] - path[i][0] == 0 and abs(result[-1][1] - path[i][1]) == 1: return True
    else: return False

def getShortcut(path):
    result = [path[-1]]
    for i in range(len(path) - 2, -1, -1):
        if calcDist(i, result): result.append(path[i])
    return result

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    graph = [list(map(int, list(input().strip()))) for _ in range(N)]
    path = BFS(0, 0)
    print(len(getShortcut(path)))