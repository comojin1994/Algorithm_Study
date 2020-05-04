from collections import deque
import sys
input = sys.stdin.readline

def checkZero(i, j):
    L = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]
    result = []
    for li in L:
        if li[0] < 0 or li[1] < 0 or li[0] > N - 1 or li[1] > M - 1: continue
        if graph[li[0]][li[1]] == 0: result.append([li[0], li[1]])
    return result

def BFS():
    result = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                result += checkZero(i, j)
    if len(result) == 0: return result, False
    return result, True

def main():
    cnt = 0
    while True:
        L, flag = BFS()
        if not flag: break
        for li in L:
            graph[li[0]][li[1]] = 1
        cnt += 1
    return cnt

if __name__ == '__main__':
    M, N = map(int, input().strip().split())
    graph = [list(map(int, input().strip().split())) for _ in range(N)]
    print(main())