import sys
input = sys.stdin.readline

N = int(input())
rings = list(map(int, input().strip().split()))
stand = rings[0]
measure = [i for i in range(1, stand+1) if stand%i == 0]

for n in rings:
    a = stand
    b = n
    if n == stand:
        continue
    else:
        for m in reversed(measure):
            if a % m == 0 and b % m == 0:
                a = a // m
                b = b // m
        print('%d/%d' % (a, b))