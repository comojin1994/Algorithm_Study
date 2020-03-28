import sys
from itertools import combinations_with_replacement as cb
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    nums = sorted(set(map(int, input().strip().split())))
    for e in sorted(set(cb(nums, M))):
        print(' '.join(map(str, e)))