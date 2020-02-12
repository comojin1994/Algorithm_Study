import sys
input = sys.stdin.readline

N = input().strip()
num = []
for s in N:
    num.append(s)
num.sort(reverse=True)
print(''.join(num))