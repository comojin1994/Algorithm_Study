import sys
from collections import deque
input = sys.stdin.readline

def func(o, deq):
    if len(o) == 2:
        if o[0] == 'push_front':
            deq.appendleft(o[1])
            return deq
        elif o[0] == 'push_back':
            deq.append(o[1])
            return deq
    else:
        if o[0] == 'pop_front':
            if len(deq) == 0:
                print(-1)
            else:
                t = deq.popleft()
                print(t)
        elif o[0] == 'pop_back':
            if len(deq) == 0:
                print(-1)
            else:
                t = deq.pop()
                print(t)
        elif o[0] == 'size':
            print(len(deq))
        elif o[0] == 'empty':
            if len(deq) == 0:
                print(1)
            else: print(0)
        elif o[0] == 'front':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq[0])
        elif o[0] == 'back':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq[-1])
        return deq


if __name__ == '__main__':
    N = int(input())
    deq = deque()
    for _ in range(N):
        o = list(input().strip().split())
        deq = func(o, deq)