import sys
input = sys.stdin.readline

if __name__ == '__main__':
    M, N, K = map(int, input().strip().split())
    signal = [list(input().strip()) for _ in range(M)]
    for i in range(M):
        cnt = 0
        while cnt != K:
            for j in range(N):
                print(signal[i][j]*K, end='')
            print()
            cnt += 1