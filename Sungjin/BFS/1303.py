import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    result = 1
    que.append((i, j))
    out = []
    while len(que) != 0:
        x, y = que.popleft()
        out.append((x,y))
        if war[x][y+1] == war[x][y]:
            if (x, y+1) not in out and (x, y+1) not in que:
                que.append((x, y+1))
                check[x][y+1] = True
                result += 1
        if war[x+1][y] == war[x][y]:
            if (x+1, y) not in out and (x+1, y) not in que:
                que.append((x+1, y))
                check[x+1][y] = True
                result += 1
        if war[x][y-1] == war[x][y]:
            if (x, y-1) not in out and (x, y-1) not in que:
                que.append((x, y-1))
                check[x][y-1] = True
                result += 1
        if war[x-1][y] == war[x][y]:
            if (x-1, y) not in out and (x-1, y) not in que:
                que.append((x-1, y))
                check[x-1][y] = True
                result += 1
    return result



if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    war = ['R'*(N+1)] + ['R' + input().strip() + 'R' for _ in range(M)] +['R'*(N+1)]
    check = [[False]*(N+2) for _ in range(M+2)]
    que = deque()
    our, ene = 0, 0
    for i in range(1, M+1):
        for j in range(1, N+1):
            if check[i][j]: continue
            check[i][j] = True
            val = bfs(i, j)

            if war[i][j] == 'W': our += val**2
            else: ene += val**2
    print(our, ene)

'''
3 3
WWW
WBW
BBB

5 5
BBBBB
BWWWB
BWBWB
BWWWB
BBBBB
'''