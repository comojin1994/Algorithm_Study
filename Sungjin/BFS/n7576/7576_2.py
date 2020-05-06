from collections import deque
import sys
input = sys.stdin.readline

def checkZero(i, j):
    L = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]
    result = []
    for li in L:
        if li[0] < 0 or li[1] < 0 or li[0] > N - 1 or li[1] > M - 1: continue
        if graph[li[0]][li[1]] == 0: result.append([li[0], li[1]])
    return result

def BFS():
    que = [deque([N]) for N in check]
    visited = [[] for _ in range(len(check))]

    while que:
        for i in range(len(check)):
            N = que[i].popleft()
            L = checkZero(N[0], N[1])
            if N not in visited:
                for li in L:
                    print(N, set(visited[i]))
                    que[i] += [set([li]) - set(visited[i])]
                    graph[li[0]][li[1]] = 1
                visited[i].append([N])
    return visited

def main():
    pass

if __name__ == '__main__':
    M, N = map(int, input().strip().split())
    graph = [list(map(int, input().strip().split())) for _ in range(N)]
    check = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1: check.append([i, j])
    print(check)
    print(BFS())