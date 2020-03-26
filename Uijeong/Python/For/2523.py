import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    for i in range(1, n+1):
        print('*' * i)
    for i in range(n-1, 0, -1):
        print('*' * i)