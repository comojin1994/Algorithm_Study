import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = input().strip()
    l = len(N)
    N = int(N)
    result = 0
    for i in range(1, l):
        result += i * 9 * 10**(i - 1)
    result += (1 + N - 10**(l - 1)) * l
    print(result)