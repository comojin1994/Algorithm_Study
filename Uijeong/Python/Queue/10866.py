import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
dq = deque()
for _ in range(n):
    op = input().strip().split()
    if op[0] == "push_front":
        dq.appendleft(op[1])
    elif op[0] == "push_back":
        dq.append(op[1])
    elif op[0] == "pop_front":
        if len(dq): print(dq.popleft())
        else: print(-1)
    elif op[0] == "pop_back":
        if len(dq): print(dq.pop())
        else: print(-1)
    elif op[0] == "size":
        print(len(dq))
    elif op[0] == "empty":
        if not len(dq): print(1)
        else: print(0)
    elif op[0] == "front":
        if len(dq): print(dq[0])
        else: print(-1)
    elif op[0] == "back":
        if len(dq): print(dq[-1])
        else: print(-1)
