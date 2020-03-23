import sys
input = sys.stdin.readline

dic = {0:0, 1:1, 2:1, 3:2}

def fibo(N):
    if N in dic.keys():
        return dic[N]

    result = fibo(N-1) + fibo(N-2)
    dic[N] = result
    return result

if __name__ == '__main__':
    N = int(input())
    print(fibo(N))