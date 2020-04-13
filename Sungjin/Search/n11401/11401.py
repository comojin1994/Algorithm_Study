import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    p = 1000000007
    facto = [0] * (N + 1)
    facto[0:3] = [1, 1, 2]
    for i in range(3, N + 1):
        facto[i] = ((i % p) * (facto[i-1] % p)) % p
    print((facto[N] * pow(facto[K]*facto[N-K], p - 2, p)) % p)