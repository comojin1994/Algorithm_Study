import sys
import math
input = sys.stdin.readline

M = int(input())
N = int(input())

li = [i for i in range(M,N+1)]

for i in range(2, int(math.sqrt(N))+1):
	for idx, j in enumerate(li):
		if li[idx] == 0:
			continue
		if li[idx] % i == 0:
			if li[idx] != i:
				li[idx] = 0
if li[0] == 1:
	li[0] = 0

result = sorted(set(li))

if len(result) == 1:
	print(-1)
elif result[1] == 1:
	print(sum(li))
	print(result[1])
else:
	print(sum(li))
	print(result[1])