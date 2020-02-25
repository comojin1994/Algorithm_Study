import sys
input = sys.stdin.readline

def check(N):
    if len(N) == 1: return True
    M = len(N) // 2
    N = list(N)
    N1 = N[:M]
    N2 = N[-M:]
    N2 = N2[::-1]
    if N1 == N2: return True
    else: return False

if __name__ == '__main__':
    while True:
        N = input().strip()
        if int(N) == 0:
            break
        if check(N): print('yes')
        else: print('no')