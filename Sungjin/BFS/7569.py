import sys
input = sys.stdin.readline

def checkMinus():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0: return False
    return True

def checkZero(i, j, k):
    L = [[i, j - 1, k], [i, j, k - 1], [i, j + 1, k],
         [i, j, k + 1], [i - 1, j, k], [i + 1, j, k]]
    result = []
    for li in L:
        if li[0] < 0 or li[0] > H - 1 or li[1] < 0 or li[1] > N - 1 or li[2] < 0 or li[2] > M - 1:
            continue
        if graph[li[0]][li[1]][li[2]] == 0:
            result.append(li)
            graph[li[0]][li[1]][li[2]] = 1
    return result

def BFS(visited):
    result = []
    for N in visited:
        result += checkZero(*N)
    return result

def main(visited):
    cnt = 0
    while True:
        visited = BFS(visited)
        if len(visited) == 0: break
        cnt += 1
    if not checkMinus(): return -1
    else: return cnt

if __name__ == '__main__':
    M, N, H = map(int, input().strip().split())
    graph = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]
    visited = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1: visited.append([i, j, k])
    print(main(visited))