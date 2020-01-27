import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().strip().split())
    dist = y - x

    n = math.ceil((math.sqrt(1 + 4 * dist) - 1) / 2)

    if dist > n ** 2:
        print(2 * n)
    else:
        print(2 * n - 1)