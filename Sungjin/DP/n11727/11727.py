import sys

input = sys.stdin.readline

N = int(input())

fac_dict = {0: 1, 1: 1}

loop = N // 2 + 1

def factorial(n):
    if n in fac_dict.keys():
        return fac_dict[n]
    else:
        result = 1
        for i in range(1, n+1):
            result = result * i
            fac_dict[i] = result
        return result

def my_func(N, k):
    result = 2**k * factorial(N - k) // (factorial(N - 2 * k) * factorial(k))
    return result

sum = 0
for i in range(loop):
    sum = sum + my_func(N, i)

print(sum % 10007)