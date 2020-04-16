import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    n = 2
    result = 0
    r = 0
    while n <= N:
        N, r = divmod(N, n)
        result += r
        n += 1
    print(result + N)