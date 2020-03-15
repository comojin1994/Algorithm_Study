import sys

input = sys.stdin.readline


if __name__ == "__main__":
    L = list(map(int, input().split()))
    sum = 0
    for li in L:
        sum += li ** 2
    print(sum % 10)