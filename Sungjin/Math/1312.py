import sys
input = sys.stdin.readline

if __name__ == '__main__':
    A, B, N = map(int, input().strip().split())
    if A < B: cnt = 0
    elif A > B: cnt = -1
    else: print(0); sys.exit(0)

    while cnt != N:
        q, r = divmod(A, B)
        if r == 0: q = 0; break
        if q == 0:
            A = r * 10
        else:
            A = r * 10
            cnt += 1
    print(q)
