import sys

input = sys.stdin.readline

t, m = map(int, input().strip().split())

if m >= 45:
    m = m - 45
else:
    t = 23 if t == 0 else t - 1
    m = 15 + m

print(t, m)