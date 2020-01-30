import sys

input = sys.stdin.readline


def check_tri(a, b, c):
    if a ** 2 == b ** 2 + c ** 2:
        return 'right'
    else:
        return 'wrong'


while True:
    num = list(map(int, input().strip().split()))
    if num == [0, 0, 0]:
        break
    max_num = max(num)
    num.remove(max_num)
    print(check_tri(max_num, num[0], num[1]))