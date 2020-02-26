import sys
import math

input = sys.stdin.readline


def minCount():
    n = math.floor(math.sqrt(d))
    if d <= n**2:
        return 2 * n - 1
    elif n**2 < d <= n**2 + n:
        return 2 * n
    elif n**2 + n < d:
        return 2 * n + 1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        d = y - x
        print(minCount())