import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    time = [300, 60, 10]
    result = []
    for t in time:
        a, T = divmod(T, t)
        result.append(a)
    if T == 0: print(' '.join(list(map(str, result))))
    else: print(-1)