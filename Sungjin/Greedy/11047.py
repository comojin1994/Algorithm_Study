import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    value = [int(input()) for _ in range(N)]
    sum = 0
    for i in range(N - 1, -1, -1):
        if value[i] > K: continue
        else:
            q, K = divmod(K, value[i])
            sum += q
        if K == 0: break
    print(sum)