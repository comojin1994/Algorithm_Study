import sys
import math
input = sys.stdin.readline


def legendre(number, p):
    cnt = 0
    i = p
    while number >= i:
        cnt += number // i
        i *= p
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt2 = legendre(n, 2) - legendre(m, 2) - legendre(n - m, 2)
    cnt5 = legendre(n, 5) - legendre(m, 5) - legendre(n - m, 5)
    print(min(cnt2, cnt5))