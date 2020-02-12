import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
li = [0 for i in range(10001)]
li[1] = 1

for i in range(2,98):
	for j in range(i*2, 10001, i):
		li[j] = 1

sum, min = 0, 0
for n in range(N, M-1, -1):
	if li[n] == 0:
		sum = sum + n
		min = n

if sum == 0:
	print(-1)
else:
	print(sum, min, sep='\n')