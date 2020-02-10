import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

def com(n,k):
    if k==0 or k==n:
        return 1
    result = com(n-1,k-1) + com(n-1,k)
    return result

print(com(N,M))