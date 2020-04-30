import sys
from collections import deque
input = sys.stdin.readline

def checkOne(i, j):
    L = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]
    result = []
    for li in L:
        if li[0] < 0 or li[1] < 0 or li[0] > N - 1 or li[1] > N - 1: continue
        if graph[li[1]][li[0]] == 1: result.append([li[0], li[1]])
    # print('re', result)
    return result

def BFS(i, j):
    que = deque([[i, j]])
    visited = []
    while que:
        n = que.popleft()
        li = checkOne(n[0], n[1])
        graph[i][j] = 0
        if n not in visited:
            for ele in li:
                if ele not in visited: que += [[ele[0], ele[1]]]
                graph[ele[1]][ele[0]] = 0
            visited.append([n])
        # print('visit', visited)
    return visited

def main():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1: print(BFS(i, j))
    return 1

if __name__ == '__main__':
    for _ in range(int(input())):
        M, N, K = map(int, input().strip().split())
        graph = [[0] * M for _ in range(N)]
        for _ in range(K):
            x, y = map(int, input().strip().split())
            graph[y][x] = 1
        main()
