import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    for i in range(2 * n):
        print('*'*(i+1), end='')


