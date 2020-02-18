import sys
from statistics import mean

input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))

maxL = max(L)
for i in range(len(L)):
    score = L[i] / maxL * 100
    L[i] = score
print(mean(L))