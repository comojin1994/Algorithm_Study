import sys
input = sys.stdin.readline

def func(i):
    global cnt
    if i+M > N:
        num = Doll[i:N] + Doll[:(i+M)%N]
        num = int(''.join(num))
    else:
        num = int(''.join(Doll[i:i+M]))
    if X <= num <= Y:
        cnt += 1
    return 1

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        X = int(''.join(input().strip().split()))
        Y = int(''.join(input().strip().split()))
        Doll = list(input().strip().split())
        cnt = 0
        for i in range(N):
            func(i)
        print(cnt)

'''
1
8 3
2 0 0
3 1 1
3 7 8 3 1 9 2 7

1
5 2
8 8
9 9
1 3 2 5 4

1
6 3
0 0 0
9 9 9
1 2 3 4 5 6
'''