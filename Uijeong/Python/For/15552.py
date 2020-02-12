import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = input().split()
    print(int(a) + int(b))