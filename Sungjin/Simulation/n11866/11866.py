import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    nums = deque([i, False] for i in range(1, N+1))
    result = []
    idx = 0
    cnt = 0
    while len(result) != N:
        t = nums.popleft()
        if not t[1]:
            cnt += 1
            if cnt == K:
                t[1] = True
                result.append(t[0])
                cnt = 0
        nums.append(t)
    print('<' + ', '.join(map(str,result)) + '>')