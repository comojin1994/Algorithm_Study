from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def BFS(s):
    que = deque([s])
    visited = []
    while que:
        n = que.popleft()
        if n not in visited:
            que += set(graph[n]) - set(visited)
            visited.append(n)
    return set(visited)

def main():
    cnt = 0
    result = set()
    for i in graph.keys():
        if i not in result:
            result = result.union(BFS(i))
            cnt += 1
    if len(graph.keys()) == N: return cnt
    else: return cnt + (N - len(graph.keys()))

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    graph = dict()
    for _ in range(M):
        n1, n2 = map(int, input().strip().split())
        if n1 not in graph.keys(): graph[n1] = []
        if n2 not in graph.keys(): graph[n2] = []
        graph[n1].append(n2)
        graph[n2].append(n1)
    if M == 0: print(N)
    else: print(main())