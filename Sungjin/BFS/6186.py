import sys
from collections import deque
input = sys.stdin.readline

def search(i, j):
    coords = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]
    result = []
    for coord in coords:
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= h or coord[1] >= w:
            continue
        if maze[coord[0]][coord[1]] == '#':
            result.append(coord)
    return result

def bfs(maze, coord):
    visited = []
    que = deque([coord])
    while que:
        node = que.popleft()
        if node in visited: continue

        maze[node[0]][node[1]] = '.'
        for c in search(*coord):
            que.append(c)
        visited.append(node)
    return maze

def solution(maze, h, w):
    answer = 0

    for i in range(h):
        for j in range(w):
            if maze[i][j] == '#':
                maze = bfs(maze, [i, j])
                answer += 1

    return answer

if __name__ == '__main__':
    h, w = map(int, input().strip().split())
    maze = [list(input().strip()) for _ in range(h)]
    print(solution(maze, h, w))