import sys
from collections import deque
input = sys.stdin.readline

def checkOne(i, j):
    L = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]
    result = []
    for li in L:
        if li[0] < 0 or li[1] < 0 or li[0] > N - 1 or li[1] > N - 1: continue
        if graph[li[0]][li[1]] == 1: result.append(li)
    return result

def BFS(i, j):
    que = deque()
    que += [[i, j]]
    visited = []
    while que:
        ele = que.popleft()
        li = checkOne(ele[0], ele[1])
        if [ele[0], ele[1]] not in visited:
            for l in li:
                if l not in visited: que += [l]
            visited.append([ele[0], ele[1]])
            graph[ele[0]][ele[1]] = 0
    return visited

def main(N):
    cnt = 0
    result = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                cnt += 1
                result.append(len(BFS(i, j)))
    return cnt, sorted(result)

if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, list(input().strip()))) for _ in range(N)]
    cnt, result = main(N)
    print(cnt)
    for e in result:
        print(e)