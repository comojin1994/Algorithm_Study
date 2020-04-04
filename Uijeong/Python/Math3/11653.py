import sys
input = sys.stdin.readline

def prime():
    sieve = [False, False] + [True] * (n-1)
    x = int(n ** 0.5)
    for i in range(2, x+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i]]


def factorization():
    global n, L
    if len(L) == 0: return
    i = 0
    while True:
        if n % L[i] == 0:
            print(L[i])
            n = n // L[i]
            if n == 1: break
        else:
            i += 1
    return

if __name__ == "__main__":
    n = int(input())
    L = prime()
    factorization()