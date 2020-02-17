import sys
input = sys.stdin.readline

def func(n):
    if n == 81:
        print_sudo(sudo)
        sys.exit(0)
    if sudo[n//9][n%9] != 0:
        func(n+1)
    else:
        for num in range(1,10):
            if row[n//9][num] or col[n%9][num] or squ[(n//27)*3 + (n//3)%3][num]:
                continue
            else:
                row[n//9][num] = col[n%9][num] = squ[(n//27)*3 + (n//3)%3][num] = True
                sudo[n//9][n%9] = num
                func(n+1)
                row[n // 9][num] = col[n % 9][num] = squ[(n//27)*3 + (n//3)%3][num] = False
                sudo[n // 9][n % 9] = 0


def print_sudo(sudo):
    for n in sudo:
        print(' '.join(map(str,n)))
    return 1

def square(i, j):
    return 3*(i//3) + j//3

if __name__ == '__main__':
    sudo = []
    col = [[False]*10 for _ in range(9)]
    row = [[False]*10 for _ in range(9)]
    squ = [[False]*10 for _ in range(9)]
    for i in range(9):
        li = list(map(int, input().strip().split()))
        for idx, n in enumerate(li):
            row[i][n] = True
            col[idx][n] = True
            squ[square(i, idx)][n] = True
        sudo.append(li)
    func(0)



'''
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 2
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 0
0 0 0 4 0 0 0 0 0
0 0 0 0 0 0 0 0 0

'''