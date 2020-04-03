import sys
input = sys.stdin.readline

def prime_factorization(n):
    temp = n
    for number in range(2, n):
        if temp == 0 or number ** 2 > n:
            break
        while temp % number == 0:
            temp //= number
            print(number)

    if temp != 1:
        print(temp)

def main():
    n = int(input().strip())
    prime_factorization(n)


if __name__ == "__main__":
    main()