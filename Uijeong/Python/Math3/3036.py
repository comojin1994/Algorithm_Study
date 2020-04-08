import sys
input = sys.stdin.readline


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def main():
    n = int(input())
    L = list(map(lambda x: x*2, list(map(int, input().split()))))
    first = L[0]
    for li in L[1:]:
        gcd_i = gcd(first, li)
        print('{}/{}'.format(first//gcd_i, li//gcd_i))


if __name__ == "__main__":
    main()