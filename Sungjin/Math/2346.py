import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    ballon = list(map(int, input().strip().split()))
    index = [i+1 for i in range(1, N)]
    result =[1]
    idx = 0
    cnt = 0
    val = ballon.pop(0)
    if val < 0: val += len(ballon) + 1
    while ballon:
        idx = cnt
        cnt = (idx + val -1) % len(ballon)
        result.append(index.pop(cnt))
        val = ballon.pop(cnt)
        if val < 0: val += len(ballon) + 1
    print(' '.join(map(str, result)))

'''
5
-5 -5 -5 -5 -5
1 5 3 2 4
'''