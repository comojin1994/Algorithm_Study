import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int ,input().strip().split())
        result = 0
        for i in range(N, M + 1):
            result += str(i).count('0')
        print(result)