import sys
from itertools import combinations as cb
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        dict = {}
        for _ in range(n):
            value, key = input().strip().split()
            if key in dict.keys(): dict[key] += 1
            else: dict[key] = 1
