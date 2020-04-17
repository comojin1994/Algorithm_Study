import sys
from collections import deque
input = sys.stdin.readline


def RD():
    op = input().strip()
    n = int(input())
    arr = input().strip()
    arr = arr[1:-1].split(',')
    dq = deque(map(int, arr)) if arr[0] else deque()

    ptr = 0
    for s in op:
        if s == 'R':
            ptr = len(dq) - 1 if ptr == 0 else 0
        elif s == 'D':
            if len(dq) == 0:
                return "error"
            if ptr == 0:
                dq.popleft()
            else:
                dq.pop()
                ptr -= 1
    return dq if ptr == 0 else reversed(dq)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        result = RD()
        if result == "error":
            print(result)
        else:
            print('[', end='')
            print(','.join(map(str, result)), end='')
            print(']')