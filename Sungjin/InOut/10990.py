import sys
input = sys.stdin.readline

def star(N):
    for i in range(N):
        print(' '*(N-i-1), end='')
        if i != 0:
            print('*', end='')
            print(' '*(2*i-1), end='')
            print('*')
        else:
            print('*')


if __name__ == '__main__':
    N = int(input())
    star(N)