import sys
from itertools import product as p
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    nums = sorted(set(map(int, input().strip().split())))

    for e in sorted(set(p(nums, repeat=M))):
        print(' '.join(map(str, e)))