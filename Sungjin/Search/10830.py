import sys
input = sys.stdin.readline

def cal_ele(A, B, N):
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    return sum % 1000

def matmul(A, B, N):
    result = [[0] * N for _ in range(N)]
    B = list(zip(*B))
    for i in range(N):
        for j in range(N):
            result[i][j] = cal_ele(A[i], B[j], N)
    return result

def matpow(m, N, B):
    if B == 1:
        return m
    elif B == 2:
        return matmul(m, m, N)
    elif B % 2 == 0:
        temp = matpow(m, N, B // 2)
        return matmul(temp, temp, N)
    else:
        return matmul(matpow(m, N, B - 1), m, N)

if __name__ == '__main__':
    N, B = map(int, input().strip().split())
    m = [list(map(int, input().strip().split())) for _ in range(N)]
    for e in matpow(m, N, B):
        for e_ in e:
            print(e_ % 1000, end=' ')
        print()