import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())

    for i in range(N):
        print(' ' * (N - 1 - i), end='')
        print('* ' * i, end='')
        print('*')