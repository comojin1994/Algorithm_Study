from collections import deque
import sys
input = sys.stdin.readline

def BFS(N, K):
    que = deque([N])
    visited = [-1] * 100001
    visited[N] = 0

    while que:
        n = que.popleft()
        cnt = visited[n]
        if n == K: break

        if n > 0 and visited[n - 1] < 0:
            visited[n - 1] = cnt + 1
            que.append(n - 1)
        if n < 100000 and visited[n + 1] < 0:
            visited[n + 1] = cnt + 1
            que.append(n + 1)
        if n < 50001 and visited[2 * n] < 0:
            visited[2 * n] = cnt + 1
            que.append(2 * n)
    return visited[K]

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    if N - K >= 0: print(N - K)
    else: print(BFS(N, K))