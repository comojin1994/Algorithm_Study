import sys
input = sys.stdin.readline

def func(idx, n, j, seq):
    global result
    if idx == n:
        result += seq
        return 1

    for i in range(j, len(nums)):
        if check[i]: continue

        check[i] = True
        seq *= nums[i]
        func(idx + 1, n, i, seq)
        check[i] = False
        seq = seq//nums[i]

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        dict = {}
        for _ in range(n):
            value, key = input().strip().split()
            if key in dict.keys(): dict[key] += 1
            else: dict[key] = 1
        result = 0
        nums = list(dict.values())
        for i in range(1, len(dict.keys()) + 1):
            check = [False] * len(nums)
            seq = 1
            func(0, i, 0, seq)
        print(result)
'''
1
6
hat headgear
sunglasses eyewear
turban headgear
mask face
sunglasses face
makeup face
'''