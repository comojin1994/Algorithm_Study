from collections import deque
import sys
input = sys.stdin.readline

def getPoint(n, K):
    if 2 * n < K:
        if n == 0: return [n + 1, n * 2]
        else: return [n * 2]
    result = [n + 1, n * 2]
    if n > 0: result.append([n - 1])
    return result

def BFS(N, K):
    que = deque([N])
    visited = [0] * (1000001)
    while que:
        n = que.popleft()
        L = getPoint(n, K)
        if n not in visited:
            for li in L:
                if li not in visited:
                    que += [li]
            visited[n] += 1
        if n == K: break
    print(visited)
    return visited[n]

if __name__ == '__main__':
    N, K = map(int, input().strip().split())

    if N > K: print(N - K)
    else: print(BFS(N, K))