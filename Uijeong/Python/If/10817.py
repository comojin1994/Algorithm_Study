import sys

input = sys.stdin.readline

L = list(map(int, input().strip().split()))
L.sort()
print(L[1])