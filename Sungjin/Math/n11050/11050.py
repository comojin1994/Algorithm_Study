import sys
input = sys.stdin.readline

fac = {0:1, 1:1, 2:2, 3:6}
N, K = map(int, input().strip().split())

def facto(n):
    if n in fac.keys():
        return fac[n]

    result = n * facto(n-1)
    fac[n] = result
    return result

facto(10)

def com(n,k):
    result = facto(n)//(facto(k)*facto(n-k))
    return result

print(com(N,K))