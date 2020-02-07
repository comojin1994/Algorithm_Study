import sys
input = sys.stdin.readline

N = int(input())
pts = []

for _ in range(N):
    pt = tuple(map(int, input().strip().split()))
    pts.append(pt)

pts = sorted(pts, key=lambda x: (x[1], x[0]))

for pt in pts:
    print('%d %d' % (pt[0], pt[1]))