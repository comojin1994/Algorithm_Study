import sys
from collections import deque
input = sys.stdin.readline

def check(n):
    idx = nums.index(n)
    if idx <= len(nums) // 2:
        return 'left'
    else:
        return 'right'

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    loc = list(map(int, input().strip().split()))
    nums = deque(i for i in range(1, N + 1))
    cnt = 0
    for n in loc:
        order = check(n)
        while nums[0] != n:
            if order == 'left':
                temp = nums.popleft()
                nums.append(temp)
                cnt += 1
            else:
                temp = nums.pop()
                nums.appendleft(temp)
                cnt += 1
        nums.popleft()
    print(cnt)