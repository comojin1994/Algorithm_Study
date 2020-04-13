import sys
input = sys.stdin.readline

def matmul(A, B):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
    return sum

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = [list(map(int, input().strip().split())) for _ in range(N)]
    M, K = map(int, input().strip().split())
    B = [list(map(int, input().strip().split())) for _ in range(M)]
    B = list(zip(*B))
    result = [[0] * K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            result[i][j] = matmul(A[i], B[j])
    for e in result:
        print(' '.join(map(str, e)))