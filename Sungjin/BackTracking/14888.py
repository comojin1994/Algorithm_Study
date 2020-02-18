import sys
input = sys.stdin.readline

def operator(n, m, o):
    if o == 0:
        return n + m
    elif o == 1:
        return n - m
    elif o == 2:
        return n * m
    else:
        return int(n / m)

def func(idx, sum):
    global min_v, max_v
    if idx == N-1:
        if sum < min_v:
            min_v = sum
        if sum > max_v:
            max_v = sum
        return 1

    for i in range(4):
        if oper[i] == 0:
            continue
        else:
            oper[i] -= 1
            temp = sum
            sum = operator(sum, nums[idx+1], i)
            func(idx+1, sum)
            sum = temp
            oper[i] += 1

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().strip().split()))
    oper = list(map(int, input().strip().split()))
    min_v, max_v = 10**10, -10**10
    func(0, nums[0])
    print(max_v)
    print(min_v)