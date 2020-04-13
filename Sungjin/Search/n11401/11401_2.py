import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    p = 1000000007
    fac = [1] * (N + 1)
    for i in range(2, N + 1):
        fac[i] = (i * fac[i-1]) % p
    print((fac[N] * pow(fac[K]*fac[N-K], p-2, p)) % p)