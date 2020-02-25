import sys
import math

input = sys.stdin.readline


def isPrime(number):
    if number == 1: return False

    sqrtN = math.floor(math.sqrt(number))
    for j in range(2, sqrtN + 1):
        if number % j == 0:
            return False
    return True


if __name__ == "__main__":
    m, n = map(int, input().split())
    for i in range(m, n + 1):
        if isPrime(i):
            print(i)