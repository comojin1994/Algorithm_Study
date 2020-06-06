import sys
input = sys.stdin.readline

if __name__ == '__main__':
    K, N, M = map(int, input().strip().split())
    print((K * N) - M if (K * N) - M > 0 else 0)