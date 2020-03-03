import sys
input = sys.stdin.readline

if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    nums = [0]
    for i in range(1, 46):
        nums += [i]*i
    print(sum(nums[A:B+1]))