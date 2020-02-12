import sys
input = sys.stdin.readline

N = int(input())
print(2**N - 1)

def move(n,s,e,m):
    if n == 1:
        print(s, e)
        return 1

    move(n-1, s, m, e)
    print(s, e)
    move(n-1, m, e, s)
    return 1

move(N,1,3,2)