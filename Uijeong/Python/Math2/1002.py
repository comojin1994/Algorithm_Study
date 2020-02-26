import sys
import math

input = sys.stdin.readline


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        r2Mr1 = math.fabs(r2 - r1)
        r2Pr1 = r2 + r1

        if r2Mr1 == 0 and x1 == x2 and y1 == y2:
            print(-1)
        elif d in [r2Mr1, r2Pr1]:
            print(1)
        elif d < r2Mr1 or d > r2Pr1:
            print(0)
        elif r2Mr1 < d < r2Pr1:
            print(2)
