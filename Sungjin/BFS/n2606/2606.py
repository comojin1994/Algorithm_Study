import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    que = deque([1])
    visited = []
    while que:
        n = que.popleft()
        if n not in visited:
            if n in graph.keys(): que += graph[n] - set(visited)
            visited.append(n)
    return visited

if __name__ == '__main__':
    N = int(input())
    Edge = int(input())
    if N == 0: print(0); sys.exit(0)
    graph = dict()
    for _ in range(Edge):
        n1, n2 = map(int, input().strip().split())
        if n1 not in graph.keys(): graph[n1] = set()
        if n2 not in graph.keys(): graph[n2] = set()
        graph[n1].add(n2); graph[n2].add(n1)
    print(len(BFS()) - 1)