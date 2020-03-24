import sys
input = sys.stdin.readline

def func(fibo):
    for i in range(4, N+1):
        fibo[i] = fibo[i-2] + fibo[i-3]
    return fibo[N]

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        fibo = [0]*101
        fibo[1] = 1
        fibo[2] = 1
        fibo[3] = 1
        N = int(input())
        print(func(fibo))