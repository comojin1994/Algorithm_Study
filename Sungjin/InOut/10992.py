import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    print(' ' * (N-1), end='')
    print('*')
    for i in range(N-2):
        print(' ' * (N - 2 - i), end='')
        print('*', end='')
        print(' ' * (2 * i + 1), end='')
        print('*')
    if N != 1:
        print('*' * (2*N - 1))