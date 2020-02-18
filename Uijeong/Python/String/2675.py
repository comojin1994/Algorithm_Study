import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, s = input().strip().split()
    n = int(n)

    for ch in s:
        print(ch * n, end='')
    print()