import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    nums = set(map(int, input().strip().split()))
    cnt = 0

    for n in nums:
        if M - n in nums: cnt = cnt + 1
    print(cnt//2)