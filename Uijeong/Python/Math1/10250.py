import sys
import math

input = sys.stdin.readline


def roomNum():
    y = math.ceil(n / h)
    x = n - h * (y - 1)
    return 100 * x + y


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        h, w, n = map(int, input().split())
        print(roomNum())
