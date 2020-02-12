import sys

input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in list(filter(lambda m: m < x, a)):
    print(i, end=' ')
