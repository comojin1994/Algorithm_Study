import sys
input = sys.stdin.readline

def star():
    for i in range(N):
        print('*'*(i+1), end='')
        print(' '*(2*(N-i-1)), end='')
        print('*' * (i+1))
    for i in range(N-2, -1, -1):
        print('*' * (i+1), end='')
        print(' ' * (2*(N - i - 1)), end='')
        print('*' * (i+1))
    return 1

if __name__ == '__main__':
    N = int(input())
    star()