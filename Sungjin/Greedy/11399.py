import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    time = sorted(list(map(int, input().strip().split())))
    result = 0
    for i in range(N):
        result += time[i] * (N - i)
    print(result)