import sys
input = sys.stdin.readline


def prime_factorization(a, b):
    tempA, tempB = a, b
    min, max = 1, 1
    for prime in range(2, a + 1):
        if tempA == tempB == 0: break
        while tempA % prime == tempB % prime == 0:
            min *= prime
            tempA //= prime
            tempB //= prime
    max = min * tempA * tempB
    return min, max


def main():
    n1, n2 = map(int, input().split())
    for li in prime_factorization(min(n1, n2), max(n1, n2)):
        print(li)


if __name__ == "__main__":
    main()
