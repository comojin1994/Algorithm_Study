import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    if n == 1: print('*')
    else:
        for i in range(2*n):
            if i % 2 == 0:
                for j in range(n):
                    if j % 2 == 0: print('*', end='')
                    else: print(' ', end='')
            else:
                for j in range(n):
                    if j % 2 == 0: print(' ', end='')
                    else: print('*', end='')
            print()