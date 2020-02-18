import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    if N == 1:
        nums = deque(n+1 for n in range(N))
    elif N % 2 == 0:
        nums = deque(n+1 for n in range(N) if n % 2 == 1)
    else:
        nums = deque(n + 1 for n in range(N) if n % 2 == 1)
        t = nums.popleft()
        nums.append(t)
    while len(nums) != 1:
        nums.popleft()
        t = nums.popleft()
        nums.append(t)
    print(nums[0])