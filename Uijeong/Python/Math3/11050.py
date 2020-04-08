import sys
from math import factorial
input = sys.stdin.readline

n, k = map(int, input().split())
print(int(factorial(n)/(factorial(k)*factorial(n-k))))