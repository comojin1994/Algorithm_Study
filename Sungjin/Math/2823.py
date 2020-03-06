import sys
input = sys.stdin.readline

def check(i, j):
    deg = 0
    if map[i][j] == '.':
        if map[i-1][j] == '.': deg += 1
        if map[i][j-1] == '.': deg += 1
        if map[i+1][j] == '.': deg += 1
        if map[i][j+1] == '.': deg += 1
    return deg

def func():
    cnt = 0
    for i in range(1, R+1):
        for j in range(1, C+1):
            deg = check(i, j)
            if deg == 1: return 1
            cnt += deg
    if cnt % 2 == 0: return 0
    else: return 1

if __name__ == '__main__':
    R, C = map(int, input().strip().split())
    map = ['X'*(C+2)] + ['X' + input().strip() + 'X' for _ in range(R)] + ['X'*(C+2)]
    print(func())

'''
9 10
XXXXXXXXXX
XX.....XXX
XX.XXXX.XX
XX.XXXX.XX
XX.XXXX.XX
XX.XXXX.XX
XX.XXXX.XX
XX......XX
XXXXXXXXXX
1

5 4
....
....
....
....
....
0
'''