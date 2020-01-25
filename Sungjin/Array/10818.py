import sys
import math

input = sys.stdin.readline

loop = int(input())
num = list(map(int, input().strip().split(' ')))

# max = -math.inf
# min = math.inf
#
# def is_min(n, min):
#     if n < min:
#         return n
#     else:
#         return min
#
# def is_max(n, max):
#     if n > max:
#         return n
#     else:
#         return max
#
# for i in range(loop):
#     min = is_min(num[i], min)
#     max = is_max(num[i], max)

print(min(num), max(num))