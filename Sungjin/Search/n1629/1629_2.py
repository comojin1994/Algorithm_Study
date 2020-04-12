import sys
input = sys.stdin.readline

if __name__ == '__main__':
    A, B, C = map(int, input().strip().split())
    print(pow(A, B, C))