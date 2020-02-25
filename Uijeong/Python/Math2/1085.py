import sys

input = sys.stdin.readline


def minToLine():
    L = [x, y, h - y, w - x]
    return min(L)


if __name__ == "__main__":
    x, y, w, h = map(int, input().split())
    print(minToLine())
