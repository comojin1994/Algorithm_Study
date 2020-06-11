from itertools import combinations
import sys, math
input = sys.stdin.readline

if __name__ == '__main__':
    nums = list(map(int, input().strip().split()))
    seri = list(combinations(nums, 3))
    min_ = 10**6
    for n1, n2, n3 in seri:
        n4 = n1*n2 // math.gcd(n1, n2)
        temp = n3*n4 // math.gcd(n3, n4)
        min_ = min(min_, temp)
    print(min_)