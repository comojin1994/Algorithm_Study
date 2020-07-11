import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    print((N * M) - 1)