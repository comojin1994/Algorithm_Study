import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, S = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    check = [0]

    for i in range(N):
        check += [nums[i] + n for n in check]
    result = check.count(S)
    if S == 0: result -= 1
    print(result)