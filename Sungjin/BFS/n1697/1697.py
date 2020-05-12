from collections import deque
import sys
input = sys.stdin.readline

def getPoint(n):
    li = [2 * n, n + 1, n - 1]
    result = [e for e in li if e < 1500001 and e > 0]
    return result

def BFS(N, K):
    que = deque([N])
    visited = [0] * (1500001)
    while que:
        n = que.popleft()
        if n == K: break
        L = getPoint(n)
        for l in L:
            if visited[l] != 0 and visited[l] < visited[n] + 1: continue
            else:
                que += [l]
                visited[l] = visited[n] + 1
    return visited[K]

if __name__ == '__main__':
    N, K = map(int, input().strip().split())

    if N >= K: print(N - K)
    else: print(BFS(N, K))