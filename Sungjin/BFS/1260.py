import sys
from collections import deque
input = sys.stdin.readline

def BFS(V):
    que = deque([V])
    visited = []
    while que:
        n = que.popleft()
        if n not in visited:
            if n in dic.keys():
                temp = list(dic[n] - set(visited))
                temp.sort()
                que += temp
            visited.append(n)
    return visited

def DFS(V):
    stack = [V]
    visited = []
    while stack:
        n = stack.pop()
        if n not in visited:
            if n in dic.keys():
                temp = list(dic[n] - set(visited))
                temp.sort(reverse=True)
                stack += temp
            visited.append(n)
    return visited

if __name__ == '__main__':
    N, M, V = map(int, input().strip().split())
    dic = {}
    if M == 0: sys.exit(0)
    for _ in range(M):
        n1, n2 = map(int, input().strip().split())
        if n1 not in dic.keys(): dic[n1] = set()
        if n2 not in dic.keys(): dic[n2] = set()
        dic[n1].add(n2)
        dic[n2].add(n1)
    print(' '.join(map(str, DFS(V))))
    print(' '.join(map(str, BFS(V))))