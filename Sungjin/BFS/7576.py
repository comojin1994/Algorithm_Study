import sys
input = sys.stdin.readline

def checkMinus(result):
    if len(result) == 0: return True
    cnt = 0
    for r in result:
        if graph[r[0]][r[1]] == -1: cnt += 1
    if cnt == len(result): return False
    return True

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
                temp = checkZero(i, j)
                if not checkMinus(temp): return result, True, False
                result += temp
    if len(result) == 0: return result, False, True
    return result, True, True

def main():
    cnt = 0
    while True:
        L, flag, flag2 = BFS()
        if not flag2: cnt = -1; break
        if not flag: break
        for li in L:
            graph[li[0]][li[1]] = 1
        cnt += 1
    return cnt

if __name__ == '__main__':
    M, N = map(int, input().strip().split())
    graph = [list(map(int, input().strip().split())) for _ in range(N)]
    print(main())