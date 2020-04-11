import sys
input = sys.stdin.readline

n, k = map(int, input().split())
L = list(range(1, n+1))
Seq = []
idx = 0
while L:
    idx = (idx + k - 1) % len(L)
    Seq.append(L[idx])
    del L[idx]

print('<'+ ', '.join(map(str, Seq)) + '>')