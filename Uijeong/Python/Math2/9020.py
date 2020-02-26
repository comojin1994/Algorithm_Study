import sys

input = sys.stdin.readline


def Partition(n):
    j = n//2
    for i in range(j, 1, -1):
        if sieve[i] and sieve[n - i]:
            return i, n - i


if __name__ == "__main__":
    sieve = [False, False] + [True] * 10000
    m = int(10001**0.5)
    for i in range(10001):
        if sieve[i]:
            for j in range(i+i, 10001, i):
                sieve[j] = False

    t = int(input())

    for _ in range(t):
        n = int(input())
        a, b = Partition(n)
        print(a, b)