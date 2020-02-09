import sys
input = sys.stdin.readline

N = int(input())
value = True
M = max(1, N-54)

while M < N:
    s = M
    for n in str(M):
        s += int(n)
    if s == N:
        value = False
        print(M)
        break
    M += 1

if value:
    print(0)