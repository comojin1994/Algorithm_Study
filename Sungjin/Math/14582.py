import sys
input = sys.stdin.readline

if __name__ == '__main__':
    J = list(map(int, input().strip().split()))
    S = list(map(int, input().strip().split()))
    r_J, r_S = 0, 0
    check = False
    for i in range(9):
        r_J += J[i]
        if r_J > r_S: check = True
        r_S += S[i]
    if r_J < r_S and check: print('Yes')
    else: print('No')