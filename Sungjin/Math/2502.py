import sys
input = sys.stdin.readline

if __name__ == '__main__':
    D, K = map(int, input().strip().split())
    dduk = [(1,0), (0,1)]
    for i in range(2, D):
        dduk += [(dduk[i-2][0] + dduk[i-1][0], dduk[i-2][1] + dduk[i-1][1])]
    f = dduk[-1][0]
    s = dduk[-1][1]
    a, b = 1, 1
    max_b = (K-f)//s
    while True:
        if f*a + s*b == K:
            print(a)
            print(b)
            break
        if b < max_b: b += 1
        else: a += 1; b = 1