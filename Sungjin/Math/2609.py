import sys
input = sys.stdin.readline

def gcd(N,M):
    while N % M != 0:
        r = N % M
        N = M
        M = r
    return M

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    gcd_v = gcd(N,M)
    print(gcd_v)
    print(N*M//gcd_v)