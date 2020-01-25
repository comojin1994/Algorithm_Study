import sys
input = sys.stdin.readline

num = []
for _ in range(9):
    num.append(int(input()))

max = max(num)
print(max)
print(num.index(max) + 1)