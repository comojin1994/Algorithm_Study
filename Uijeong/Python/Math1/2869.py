import sys
import math

input = sys.stdin.readline


def day():
    n = math.ceil((v - a) / (a - b)) + 1
    return n


if __name__ == "__main__":
    a, b, v = map(int, input().split())
    print(day())
