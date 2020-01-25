import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().strip().split())

def cal_day(A, B, V):
    day = math.ceil((V-A)/(A-B)) + 1
    return day

print(cal_day(A, B, V))