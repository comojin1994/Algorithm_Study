import sys
import math
input = sys.stdin.readline

M, N = map(int, input().strip().split())

li = [0 for i in range(N+1)]
li[0] = 1
li[1] = 1

for i in range(2, int(math.sqrt(N))+1):
	for j in range(i*2, N+1, i):
		li[j] = 1

for idx, n in enumerate(li):
	if n == 0 and idx >= M:
		print(idx)