import sys, heapq
input = sys.stdin.readline

if __name__ == '__main__':
    nums = []
    for _ in range(int(input())):
        n = int(input())
        if n == 0:
            if len(nums) == 0: print(0)
            else: print(heapq.heappop(nums)[1])
        else:
            heapq.heappush(nums, (-n, n))