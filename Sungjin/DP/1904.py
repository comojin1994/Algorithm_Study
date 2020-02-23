import sys
input = sys.stdin.readline

def func(fibo):
    for n in range(3, N+1):
        fibo[n] = ((fibo[n-1]%15746) + (fibo[n-2]%15746))%15746
    return fibo[N]

if __name__ == '__main__':
    N = int(input())
    fibo = [1]*1000001
    fibo[1] = 1
    fibo[2] = 2
    print(func(fibo))