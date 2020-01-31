import sys

input = sys.stdin.readline

dict = {0: 1, 1: 1}

N = int(input())


def factorial(n):
    if n in dict.keys():
        return dict[n]
    result = n * factorial(n - 1)
    return result


print(factorial(N))