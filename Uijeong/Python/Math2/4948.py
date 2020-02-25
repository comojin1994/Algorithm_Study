import sys

input = sys.stdin.readline


def isPrime(n, m):
    sieve = [False, False] + [True] * (m - 1)

    sqM = int(m ** 0.5)
    for i in range(sqM + 1):
        if sieve[i]:
            for j in range(i+i, m+1, i):
                sieve[j] = False
    return [i for i in range(n, m + 1) if sieve[i]]


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            print(len(isPrime(n + 1, 2*n)))

