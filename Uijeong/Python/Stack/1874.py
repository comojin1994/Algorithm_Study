import sys
input = sys.stdin.readline


def stack():
    s1, s2 = [], []
    i = 0
    for x in range(1, n+1):
        s1.append(x)
        s2.append('+')
        while s1:
            if s1[-1] == L[i]:
                del s1[-1]
                s2.append('-')
                i += 1
            else: break
    if s1: print('NO')
    else: print('\n'.join(s2))



if __name__ == "__main__":
    n = int(input())
    L = [int(input()) for _ in range(n)]
    stack()