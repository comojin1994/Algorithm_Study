import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    h, w = 0, 0
    H, W, N = map(int, input().strip().split())
    w = math.ceil(N / H)
    if N % H == 0:
        h = H
    else:
        h = N % H

    if w < 10:
        room = int(str(h) + '0' + str(w))
    else:
        room = int(str(h) + str(w))
    print(room)