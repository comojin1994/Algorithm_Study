from collections import deque
import sys
input = sys.stdin.readline

def checkZero(x, y, cnt):
    L = [[x - 1, y, cnt], [x, y - 1, cnt], [x + 1, y, cnt], [x, y + 1, cnt]]
    result = []
    for li in L:
        if li[0] < 0 or li[1] < 0 or li[0] > N - 1 or li[1] > M - 1: continue
        if graph[li[0]][li[1]] == 0:
            result.append(li)
            graph[li[0]][li[1]] = 2
        if (graph[li[0]][li[1]] == 1 or graph[li[0]][li[1]] == 2) and cnt == 0:
            result.append([li[0], li[1], li[2] + 1])
    return result

def BFS():
    que = deque([[0, 0, 0]])
    visited = []
    graph[0][0] = 2
    while que:
        n = que.popleft()
        if n not in visited:
            L = checkZero(*n)
            for ele in L:
                if ele not in visited: que.append(ele)
            visited.append(n)
            if n == [N - 1, M - 1]: break
    print(visited)
    return visited

def getPath(visited):
    result = [visited[-1]]
    for i in range(len(visited) - 2, -1, -1):
        if abs(result[-1][0] - visited[i][0]) + abs(result[-1][1] - visited[i][1]) == 1:
            result.append(visited[i])
    if len(result) < N + M: return -1
    else: return len(result)

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    graph = [list(map(int, list(input().strip()))) for _ in range(N)]
    print(getPath(BFS()))

'''
6 4
0000
1110
1000
0000
0111
0000
'''