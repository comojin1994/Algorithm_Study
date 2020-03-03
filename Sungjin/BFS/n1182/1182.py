import sys
from itertools import combinations as cb
input = sys.stdin.readline

if __name__ == '__main__':
    N, S = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    cnt = 0
    for i in range(1, len(nums)+1):
        for li in list(cb(nums, i)):
            if sum(li) == S: cnt += 1
    print(cnt)