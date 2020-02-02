import sys
input = sys.stdin.readline

N = int(input())
peoples = []

for _ in range(N):
	peoples.append(list(map(int, input().strip().split())))

l = len(peoples)
rank = [1 for _ in range(l)]

for i in range(l):
	for j in [n for n in range(l) if n != i]:
		if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
			rank[i] += 1

for n in rank:
	print(n, end=' ')