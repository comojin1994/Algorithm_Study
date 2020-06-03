import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    nums = set(map(int, input().strip().split()))
    x = int(input())
    cnt = 0
    for n in nums:
        if x - n in nums: cnt += 1
    print(cnt // 2)