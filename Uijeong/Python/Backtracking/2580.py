import sys
import copy

input = sys.stdin.readline


def zeroList(L):
    cnt = 0
    for i, li in enumerate(L):
        for j, num in enumerate(li):
            if num == 0:
                ans = ansList(i, j, L)
                if len(ans) == 1:
                    cnt += 1
                    L[i][j] = ans[0]
    if cnt > 0:
        zeroList(L)
    else:
        d = []
        for i, li in enumerate(L):
            for j, num in enumerate(li):
                if num == 0:
                    d.append([(i, j), ansList(i, j, L)])
        return d


def ansList(i, j, L):
    row = copy.deepcopy(L[i])
    col = [li[j] for li in L]
    sqRow, sqCol = i // 3 * 3, j // 3 * 3
    square = sum([li[sqCol:sqCol + 3] for li in L[sqRow:sqRow + 3]], [])
    return list(set([i for i in range(1, 10)]) - set(row + col + square))


def adjacent(i, j, ni, nj):
    if i == ni or j == nj or (i // 3 == ni // 3 and j // 3 == nj // 3):
        return True
    else:
        return False


def dfs(x, L, zeroL):
    # print(x)
    if x == len(zeroL):     # break
        for li in L:
            print(' '.join(map(str, li)))
        sys.exit(0)

    tmpL = copy.deepcopy(L)
    tmpZeroL = copy.deepcopy(zeroL)
    # print(tmpZeroL)
    i, j = tmpZeroL[x][0]
    tmpZeroL[x][1] = list(set(ansList(i, j, tmpL)))
    for ans in tmpZeroL[x][1]:
        # print(i, j, ans)
        tmpL[i][j] = ans
        # for idx, ((ni, nj), li) in enumerate(zeroL[x+1:]):
        #     if (ni, nj) == (i, j):
        #         continue
        #     tmpZeroL[x+1+idx][1] = list(set(ansList(ni, nj, tmpL)))
        #     print(tmpZeroL)
        # if len(tmpZeroL[x+1+idx][1]) > 0:
        # print(ans)
        dfs(x + 1, tmpL, tmpZeroL)


if __name__ == "__main__":
    # zL = zeroList(L)
    # if len(zL) > 0:
        # zL = sorted(zL, key=lambda x: len(x[1]))
    dfs(0, L, L)
    # else:
    #     for li in L:
    #         print(' '.join(map(str, li)))

'''
0 5 2 0 0 7 0 9 8
1 0 6 0 5 8 0 0 4
0 0 0 0 1 0 7 0 0
0 6 0 0 0 3 2 1 0
0 0 8 1 0 5 6 0 0
0 1 9 6 0 0 0 3 0
0 0 3 0 4 0 0 0 0
6 0 0 2 8 9 0 0 0
9 2 0 7 0 0 4 8 0

7 0 0 1 4 0 0 0 8
0 2 9 3 0 0 0 0 7
0 1 0 5 0 0 4 6 0
8 0 1 0 6 3 5 0 0
0 9 0 2 0 0 0 8 0
0 0 7 9 0 0 6 0 1
0 6 4 0 0 1 0 7 0
5 0 0 0 0 7 3 1 0
1 0 0 0 2 5 0 0 6

0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''