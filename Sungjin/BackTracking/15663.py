import sys
from itertools import permutations as pm
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    for e in sorted(set(pm(nums, M))):
        print(' '.join(map(str, e)))