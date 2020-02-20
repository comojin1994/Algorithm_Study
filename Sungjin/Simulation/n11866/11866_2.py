import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    nums = [i for i in range(1,N+1)]
    result = []
    idx = 0
    cnt = 0
    while nums:
        idx = cnt
        cnt = (idx + K - 1) % len(nums)
        result.append(nums.pop(cnt))
    print('<' + ', '.join(map(str, result)) + '>')