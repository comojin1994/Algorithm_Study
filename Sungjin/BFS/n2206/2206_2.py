import sys
import copy
from collections import deque
input = sys.stdin.readline

def select(graph, i, j):
    result = []
    wall_break = []
    coords = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]
    for coord in coords:
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= N or coord[1] >= M: continue
        if graph[coord[0]][coord[1]] == '0':
            result.append(coord)
        else:
            wall_break.append(coord)
    return result, wall_break

def decode_root(visited):
    past = visited[-1]
    result = [past]
    for idx, node in enumerate(reversed(visited)):
        if idx == 0: continue
        if abs(sum(past) - sum(node)) == 1:
            result.append(node)
            past = node
    return result

def bfs(graph, N, M, start, cnt):
    if cnt > 1: return []
    visited = []
    que = deque([start])
    while que:
        node = que.popleft()
        if node == [N - 1, M - 1]:
            visited.append(node)
            break
        if node in visited or node in que: continue
        coords, walls = select(graph, *node)
        for c in coords:
            que.append(c)
        visited.append(node)

        for wall in walls:
            new_graph = copy.deepcopy(graph)
            new_graph[wall[0]][wall[1]] = '0'
            break_root = bfs(new_graph, N, M, wall, cnt + 1)
            print('break root : ', break_root)
            print('visited : ', decode_root(visited))
            print('final : ', break_root + decode_root(visited))
            print('=' * 50)

    return decode_root(visited)

def solution(graph, N, M):
    results = []
    start = [0 ,0]
    bfs(graph, N, M, start, 0)

    answer = 100000000

    return answer

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    graph = [list(input().strip()) for _ in range(N)]
    print(solution(graph, N, M))

'''
6 4
0000
1110
1000
0000
0111
0000
'''