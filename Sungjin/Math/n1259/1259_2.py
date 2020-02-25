import sys
input = sys.stdin.readline

def check(N):
    return N==N[::-1]

if __name__ == '__main__':
    while True:
        N = input().strip()
        if int(N) == 0:
            break
        if check(N): print('yes')
        else: print('no')