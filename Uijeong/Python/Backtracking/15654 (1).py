import sys
from itertools import permutations
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    for li in permutations(arr, m):
        print(' '.join(map(str, li)))
