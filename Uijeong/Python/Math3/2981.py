import sys
input = sys.stdin.readline


def factor(n):
    if n == 1: return
    temp = [n]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(i, end=' ')
            if i * i != n:
                temp.append(n // i)
    print(' '.join(map(str, reversed(temp))))


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def main():
    n = int(input())
    L = [int(input()) for _ in range(n)]
    L.sort()
    gcd_i = L[1] - L[0]
    for i in range(2, n):
        gcd_i = gcd(gcd_i, L[i] - L[i-1])
    factor(gcd_i)

if __name__ == "__main__":
    main()
