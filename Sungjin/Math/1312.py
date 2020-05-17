import sys
input = sys.stdin.readline

if __name__ == '__main__':
    A, B, N = map(int, input().strip().split())
    cnt = 0
    if A >= B: A = A % B

    while cnt != N + 1:
        Q = A // B
        r = A % B
        A = r * 10
        cnt += 1
    print(Q)