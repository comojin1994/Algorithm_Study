import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    result = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]] + [[0]*10 for _ in range(N-1)]

    for i in range(1, N):
        for j in range(10):
            if j == 0: result[i][j] = result[i-1][j+1]
            elif j == 9: result[i][j] = result[i-1][j-1]
            else:
                result[i][j] = result[i-1][j-1] % 10**9 + result[i-1][j+1] % 10**9

    print(sum(result[N-1]) % 10**9)