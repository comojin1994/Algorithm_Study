import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    for i in range(n * 2 - 1, 0, -2):
        j = (n * 2 - 1 - i) // 2
        print(' ' * j, end='')
        print('*' * i)
    for i in range(3, n * 2, 2):
        j = (n * 2 - 1 - i) // 2
        print(' ' * j, end='')
        print('*' * i)