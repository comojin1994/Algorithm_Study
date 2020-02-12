import sys

input = sys.stdin.readline

a, b = map(int, input().strip().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)