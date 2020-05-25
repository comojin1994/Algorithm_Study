import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    Pi = sorted([int(input()) for _ in range(M)])
    value = [0] * M
    for i in range(M):
        if N >= M:
            value[i] = Pi[i] * (M - i)
        else:
            value[i] = Pi[i] * N if N + i <= M else Pi[i] * (M - i)
    print(Pi[value.index(max(value))], max(value))