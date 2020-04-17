from collections import deque
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())
    pick = list(map(int, input().split()))
    dq = deque(range(1, n + 1))
    cnt = 0
    idx = 0
    while idx < m:
        if pick[idx] == 1:
            dq.popleft()
            pick[idx:] = list(map(lambda x: x - 1, pick[idx:]))
            idx += 1
        else:
            if pick[idx] - 1 <= len(dq) // 2:
                dq.append(dq.popleft())
                pick[idx:] = list(map(lambda x: x - 1, pick[idx:]))
                for i, p in enumerate(pick):
                    if p == 0:
                        pick[i] = len(dq)
                cnt += 1
            else:
                dq.extendleft([dq.pop()])
                pick[idx:] = list(map(lambda x: x + 1, pick[idx:]))
                for i, p in enumerate(pick):
                    if p == len(dq) + 1:
                        pick[i] = 1
                cnt += 1
    print(cnt)

