import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
row = [sum(i) for i in stat]
col = [sum(i) for i in zip(*stat)]
newstat = [i+ j for i, j in zip(row, col)]
allstat = sum(newstat) // 2
newstat.sort()
newstat[1::2] = newstat[-1::-2]

mins = 65535
for l in cb(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l)))
    if not mins:
        print(0)
        break
else:
    print(mins)