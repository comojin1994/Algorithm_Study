import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip().split())

if B >= C:
    print(-1)
else:
    print((A // (C - B)) + 1)