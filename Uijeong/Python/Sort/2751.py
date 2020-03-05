import sys

input = sys.stdin.readline

n = int(input())

L = [int(input()) for _ in range(n)]

L.sort()
for li in L:
    print(li)