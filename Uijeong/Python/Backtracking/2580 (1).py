import sys

input = sys.stdin.readline

sys.setrecursionlimit(5000)


def dfs(d):
    if d == 81:
        for l in L:
            print(' '.join(map(str, l)))
        exit(0)

    x = d // 9
    y = d % 9
    # 들어갈 숫자 찾기
    if L[x][y] == 0:
        for i in range(1, 10):
            if not row[x][i] and not col[y][i] and not square[x // 3 * 3 + y // 3][i]:
                L[x][y] = i
                row[x][i] = col[y][i] = square[x // 3 * 3 + y // 3][i] = True
                dfs(d + 1)
                L[x][y] = 0
                row[x][i] = col[y][i] = square[x // 3 * 3 + y // 3][i] = False
    else:
        dfs(d + 1)


if __name__ == "__main__":
    L = [list(map(int, input().split())) for _ in range(9)]
    row = [[False] * 10 for _ in range(9)]
    col = [[False] * 10 for _ in range(9)]
    square = [[False] * 10 for _ in range(9)]

    for i, li in enumerate(L):
        for j, num in enumerate(li):
            if num != 0:
                row[i][num] = True
                col[j][num] = True
                sqRow, sqCol = i // 3 * 3, j // 3
                square[sqRow + sqCol][num] = True
    dfs(0)
