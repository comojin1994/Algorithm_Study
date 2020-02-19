import sys
input = sys.stdin.readline

dic = {0:0, 1:1}
dic_c = {0:[1, 0], 1:[0, 1]}

def fibo(N):
    if N in dic.keys():
        return dic[N]
    result = fibo(N-1) + fibo(N-2)
    dic_c[N] = [dic_c[N-1][0] + dic_c[N-2][0], dic_c[N-1][1] + dic_c[N-2][1]]
    dic[N] = result
    return result

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        res = [0, 0]
        N = int(input())
        fibo(N)
        print(' '.join(map(str, dic_c[N])))