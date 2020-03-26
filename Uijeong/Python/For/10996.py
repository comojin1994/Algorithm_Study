import sys
import math
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        for j in range(math.ceil(n/2)):
            print('*', end=' ')
        print()
        print(' ', end='')
        for j in range(n//2):
            print('*', end=' ')
        print()