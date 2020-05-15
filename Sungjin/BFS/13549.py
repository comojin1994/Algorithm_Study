from collections import deque
import sys
input = sys.stdin.readline

def BFS(N, K):
    que = deque([N])
    visited = [-1] * 100001
    L = [N * (2 ** k) for k in range(17) if N * (2 ** k) < 100000]
    for n in L:
        visited[n] = 0

    while que:
        n = que.popleft()
        cnt = visited[n]
        if n < 50001 and (visited[2 * n] < 0 or visited[2 * n] > cnt):
            visited[2 * n] = cnt
            que.append(2 * n)
        if n < 100000 and (visited[n + 1] < 0 or visited[n + 1] > cnt):
            visited[n + 1] = cnt + 1
            que.append(n + 1)
        if n > 0 and (visited[n - 1] < 0 or visited[n - 1] > cnt):
            visited[n - 1] = cnt + 1
            que.append(n - 1)
    print(visited[:10])
    return visited[K]

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    if N - K >= 0: print(N - K)
    else: print(BFS(N, K))

'''
0 100000
6
'''