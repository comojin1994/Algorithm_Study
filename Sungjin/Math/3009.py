import sys

input = sys.stdin.readline

pts_x = dict()
pts_y = dict()

for _ in range(3):
    x, y = map(int, input().strip().split())
    if x in pts_x.keys():
        pts_x[x] += 1
    else:
        pts_x[x] = 1

    if y in pts_y.keys():
        pts_y[y] += 1
    else:
        pts_y[y] = 1

x = list(pts_x.items())
y = list(pts_y.items())
print([i[0] for i in x if i[1] == 1][0], [i[0] for i in y if i[1] == 1][0])