import sys
input = sys.stdin.readline

H, M = map(int, input().strip().split(' '))

if H != 0:
    if M >= 45:
        print(H, M-45)
    else:
        print(H-1, 15 + M)
else:
    if M >= 45:
        print(H, M-45)
    else:
        print(23, 15 + M)