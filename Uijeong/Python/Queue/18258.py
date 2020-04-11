import sys
input = sys.stdin.readline

n = int(input())
S = [input().strip().split() for _ in range(n)]
L = []
idx = 0
for s in S:
    if s[0] == 'push':
        L.append(s[1])
    elif s[0] == 'pop':
        if len(L) > idx: print(L[idx]); idx += 1
        else: print(-1)
    elif s[0] == 'size':
        print(len(L) - idx)
    elif s[0] == 'empty':
        print(0) if len(L) > idx else print(1)
    elif s[0] == 'front':
        print(L[idx]) if len(L) > idx else print(-1)
    elif s[0] == 'back':
        print(L[-1]) if len(L) > idx else print(-1)