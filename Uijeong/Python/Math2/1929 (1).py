import sys

input = sys.stdin.readline


def isPrime(m, n):
    # 소수찾기 알고리즘 에라토스테네스의 체 이용
    sieve = [False, False] + [True] * (n - 1)

    x = int(n ** 0.5)
    for i in range(2, x + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(m, n) if sieve[i] == True]


if __name__ == "__main__":
    m, n = map(int, input().split())
    for i in isPrime(m, n+1):
        print(i)