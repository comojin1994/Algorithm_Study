import sys
input = sys.stdin.readline

def star(N):
    for i in range(1, N+1):
        print(' '*(N-i), end='')
        print('*'*i)
    for i in range(N-1, 0,-1):
        print(' '*(N-i), end='')
        print('*'*i)
    return 1

if __name__ == '__main__':
    N = int(input())
    star(N)