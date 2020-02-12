import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    nums = sorted(list(map(int, input().strip().split())))
    print(nums[0] * nums[N-1])