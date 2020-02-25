import sys
import math

input = sys.stdin.readline

def isPrime(number):
    if number == 1: return False

    n = math.floor(math.sqrt(number))

    for k in range(2, n + 1):
        if number % k == 0:
            return False
    return True


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    L = []
    for i in range(m, n + 1):
        if isPrime(i):
            L.append(i)
    if len(L) == 0:
        print(-1)
    else:
        print(sum(L))
        print(min(L))
