import sys
from collections import deque
input = sys.stdin.readline

def checkOne(i, j):
    L = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]
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
    return visited

def main():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1: BFS(i, j); cnt += 1
    return cnt

if __name__ == '__main__':
    for _ in range(int(input())):
        M, N, K = map(int, input().strip().split())
        graph = [[0] * M for _ in range(N)]
        for _ in range(K):
            x, y = map(int, input().strip().split())
            graph[y][x] = 1
        print(main())

'''
10 8 17
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 1, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''