import sys
input = sys.stdin.readline

N = int(input())
result = [0 for _ in range(10001)]

for _ in range(N):
    n = int(input())
    result[n] += 1

for idx, n in enumerate(result):
    if n != 0:
        for m in range(n):
            print(idx)