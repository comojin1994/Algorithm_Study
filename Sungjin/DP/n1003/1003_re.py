import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp_0 = [0] * (N + 2)
        dp_1 = [0] * (N + 2)
        dp_0[0] = 1
        dp_1[1] = 1
        for i in range(2, N+1):
            dp_0[i] = dp_0[i-1] + dp_0[i-2]
            dp_1[i] = dp_1[i-1] + dp_1[i-2]
        print(dp_0[N], dp_1[N])