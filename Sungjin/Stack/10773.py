import sys
input = sys.stdin.readline

K = int(input())
num = []

for _ in range(K):
    n = int(input())
    if n == 0:
        num.pop()
    else:
        num.append(n)
print(sum(num))