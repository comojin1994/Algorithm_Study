import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == '__main__':
    nan = [int(input()) for _ in range(9)]
    for ele in list(combinations(nan, 7)):
        if sum(ele) == 100:
            for e in sorted(ele):
                print(e)
            break