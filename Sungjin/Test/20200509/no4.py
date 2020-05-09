from collections import deque
import sys
input = sys.stdin.readline

def checkZero(i, j):
    L = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]
    result = []
    for li in L:
        if li[0] < 0 or li[1] < 0 or li[0] > N - 1 or li[1] > N - 1: continue
        if board[li[0]][li[1]] == 0:
            result.append(li)
    return result

def BFS():
    que = deque([[0, 0]])
    visited = []
    while que:
        n = que.popleft()
        li = checkZero(*n)
        board[n[0]][n[1]] = 1
        if n not in visited:
            for l in li:
                if l not in visited: que += [l]
            visited.append(n)
            if n == [N - 1, N - 1]: break
    return visited

def calcDist(i, result):
    if abs(result[-1][0] - path[i][0]) == 1 and result[-1][1] - path[i][1] == 0: return True
    elif result[-1][0] - path[i][0] == 0 and abs(result[-1][1] - path[i][1]) == 1: return True
    else: return False

def getShortcut(path):
    result = [path[-1]]
    for i in range(len(path) - 2, -1, -1):
        if calcDist(i, result): result.append(path[i])
    return result

def getConer(result):
    cnt = 0
    flag = 'x' if result[1][0] == result[0][0] else 'y'
    flag_n = 0
    for i in range(1, len(result)):
        if result[i][0] == result[i-1][0]:
            flag_n = 'x'
        elif result[i][1] == result[i-1][1]:
            flag_n = 'y'
        if flag != flag_n:
            cnt += 1
        flag = flag_n
    return cnt

if __name__ == '__main__':
    N = int(input())
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        board[i] = list(map(int, input().strip().split()))
    path = BFS()
    path = getShortcut(path)
    print(len(path)*100 + getConer(path)*500)


'''
3
0 0 0
0 0 0
0 0 0

8
0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0
0 0 0 0 1 0 0 0
0 0 0 1 0 0 0 1
0 0 1 0 0 0 1 0
0 1 0 0 0 1 0 0
1 0 0 0 0 0 0 0

4
0 0 1 0
0 0 0 0
0 1 0 1
1 0 0 0

6
0 0 0 0 0 0
0 1 1 1 1 0
0 0 1 0 0 0
1 0 0 1 0 1
0 1 0 0 0 1
0 0 0 0 0 0
'''