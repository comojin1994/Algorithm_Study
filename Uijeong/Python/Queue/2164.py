import sys
input = sys.stdin.readline

n = int(input())
L = list(range(1, n+1))
idx = 0
while idx+1 < len(L):
    if idx % 2:
        L.append(L[idx])
    idx = idx + 1
print(L[idx])