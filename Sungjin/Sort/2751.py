import sys
input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    li.append(int(input()))

li.sort()
for n in li:
    print(n)