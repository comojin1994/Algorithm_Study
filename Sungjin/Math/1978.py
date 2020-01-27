import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int, input().strip().split()))
count = 0


def is_prime(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, n):
            if n % i == 0:
                return 0
                break
        return 1


for n in num:
    if is_prime(n) == 1:
        count = count + 1
    else:
        continue
print(count)