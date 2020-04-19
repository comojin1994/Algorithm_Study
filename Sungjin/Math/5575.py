import sys
input = sys.stdin.readline

def getTime(A):
    start, end = A[:3], A[3:]
    s = end[2] - start[2]
    if s < 0:
        s += 60
        end[1] -= 1
    m = end[1] - start[1]
    if m < 0:
        m += 60
        end[0] -= 1
    t = end[0] - start[0]
    return t, m, s

if __name__ == '__main__':
    for _ in range(3):
        for n in getTime(list(map(int, input().strip().split()))):
            print(n, end=' ')
        print()