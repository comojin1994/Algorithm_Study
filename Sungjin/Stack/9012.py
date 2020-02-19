import sys
input = sys.stdin.readline

def func(string):
    sum = 0
    for s in string:
        if s == '(':
            sum += 1
        elif s == ')':
            sum -= 1

        if sum < 0:
            return 'NO'
    if sum == 0:
        return 'YES'
    elif sum > 0:
        return 'NO'

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        string = list(input().strip())
        print(func(string))