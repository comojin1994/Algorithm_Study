import sys
input = sys.stdin.readline

def get_AB(a1, a2, a3):
    if a1==a2: return 1, 0, False
    a = (a3 - a2) // (a2 - a1)
    b = (a2**2 - a3*a1) // (a2 - a1)
    if a - ((a3 - a2) / (a2 - a1)) != 0: return a, b, True
    else: return a, b, False

def func(N):
    if len(seq) == 1: return 'A'
    elif len(seq) == 2:
        if seq[0] == seq[1]: return seq[1]
        else: return 'A'

    a, b, check = get_AB(seq[0], seq[1], seq[2])
    if check: return 'B'
    for i in range(2, N):
        if seq[i] == seq[i-1]*a + b: continue
        else: return 'B'

    return seq[N-1]*a + b

if __name__ == '__main__':
    N = int(input())
    seq = list(map(int, input().strip().split()))
    print(func(N))