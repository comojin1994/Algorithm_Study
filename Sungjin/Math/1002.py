import sys
import math
input = sys.stdin.readline

def cal_dist(x1,y1,x2,y2):
	dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
	return dist

T = int(input())
for _ in range(T):
	x1,y1,r1,x2,y2,r2 = map(int, input().strip().split())
	dist = cal_dist(x1,y1,x2,y2)
	if dist == 0:
		if r1 == r2:
			print(-1)
		else:
			print(0)
	elif dist == abs(r2-r1):
		print(1)
	elif dist < abs(r2-r1):
		print(0)
	elif dist == r1+r2:
		print(1)
	elif dist < r1+r2:
		print(2)
	elif dist > r1+r2:
		print(0)
	else:
		print('Error')