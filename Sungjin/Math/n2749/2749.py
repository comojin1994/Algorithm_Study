# 피사노 주기
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    P = 15 * (10 ** 5)
    M = 10**6
    fibo = [0 for _ in range(P)]
    fibo[1], fibo[2] = 1, 1
    for i in range(3, P):
        fibo[i] = ((fibo[i-1] % M) + (fibo[i-2] % M)) % M
    print(fibo[n % P])