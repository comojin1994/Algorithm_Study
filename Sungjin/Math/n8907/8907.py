import sys
input = sys.stdin.readline

def dot(row, col):
    sum_ = 0
    for i in range(N):
        sum_ += row[i] * col[i]
    return sum_

def matmul(M):
    result = [[0] * N for _ in range(N)]
    sum_ = 0
    r = 0
    for row in M:
        c = 0
        for col in zip(*M):
            if r <= c:
                result[r][c] = dot(row, col)
                result[c][r] = result[r][c]
            c += 1
        sum_ += dot(result[r], list(zip(*M))[r])
        r += 1
    return sum_ // 6

if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        graph_r = [[0] * N for _ in range(N)]
        graph_b = [[0] * N for _ in range(N)]
        for i in range(N - 1):
            li = list(map(int, input().strip().split()))
            graph_r[i][i+1:] = li
            for j in range(i + 1, N):
                graph_r[j][i] = graph_r[i][j]
        for i in range(N):
            for j in range(N):
                if i != j: graph_b[i][j] = 1 if graph_r[i][j] == 0 else 0

        print(matmul(graph_r) + matmul(graph_b))