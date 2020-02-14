import sys
input = sys.stdin.readline

def star(N):
    for i in range(1, N+1):
        print('*'*i)
    for i in range(N-1,0,-1):
        print('*'*i)

if __name__ == '__main__':
    N = int(input())
    star(N)