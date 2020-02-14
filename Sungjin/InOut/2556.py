import sys
input = sys.stdin.readline

def star(N):
    for i in range(N):
        print('*'*N)

if __name__ == '__main__':
    N = int(input())
    star(N)