import sys
from statistics import mean

input = sys.stdin.readline

c = int(input())

for i in range(c):
    L = list(map(int, input().split()))
    n, L = L[0], L[1:]
    meanL = mean(L)
    rate = len(list(filter(lambda x: x > meanL, L))) / len(L) * 100
    print("{:.3f}%".format(round(rate, 3)))
