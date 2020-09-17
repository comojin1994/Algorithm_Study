import sys
from collections import deque
input = sys.stdin.readline

def solution(graph):
    answer = 0
    visited = [1]
    que = deque(graph[1])

    while que:
        node = que.popleft()
        if node in visited: continue
        for n in graph[node]:
            que.append(n)
        visited.append(node)
        answer += 1

    return answer

if __name__ == '__main__':
    N = int(input())
    graph = dict()
    for _ in range(int(input())):
        n1, n2 = map(int, input().strip().split())
        if n1 not in graph.keys(): graph[n1] = []
        if n2 not in graph.keys(): graph[n2] = []
        graph[n1].append(n2)
        graph[n2].append(n1)
    print(solution(graph))