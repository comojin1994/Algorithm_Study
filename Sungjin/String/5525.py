import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    S = input().strip()
    P = 'I' + 'OI'*N
    start = False
    check = 0
    cnt, result = 0, 0
    for i, s in enumerate(S):
        if start:
            if s == 'O' and check == 1: check += 1
            elif s == 'I' and check == 2: cnt += 1
            else:
                if cnt >= N: result += cnt - N + 1
                start = False
                check, cnt = 0, 0
        if s == 'I': start = True; check = 1
    if cnt >= N: result += cnt - N + 1
    print(result)


'''
2
25
OOIOIIOIOIOIOIOIOIOIOOIOI
6

4
100
IIOIOIOIOIOIOOOOIOIOIOIOOIIOIOIOIOIOIOIIOIOIOIOOOIIOIOIOIOIOIOOOOIOIOIOIOIOIOOIIIIOIOIOIOIOIIOIOIOIO
11
'''