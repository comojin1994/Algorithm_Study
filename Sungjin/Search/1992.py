import sys
input = sys.stdin.readline

def get_New(video, x, y):
    result = []
    for i in range(x[0], y[0]):
        result.append(video[i][x[1]:y[1]])
    return result

def isAll(video, N):
    set_init = video[0][0]
    for i in range(N):
        for j in range(N):
            if video[i][j] != set_init: return False
    return True

def check(video, N):
    tf = isAll(video, N)
    if tf:
        return str(video[0][0])
    else:
        a = check(get_New(video, (0, 0), (N // 2, N // 2)), N // 2)
        b = check(get_New(video, (0, N // 2), (N // 2, N)), N // 2)
        c = check(get_New(video, (N // 2, 0), (N, N // 2)), N // 2)
        d = check(get_New(video, (N // 2, N // 2), (N, N)), N // 2)
        if a and b and c and d:
            return '('+a+b+c+d+')'

if __name__ == '__main__':
    N = int(input())
    video = [list(map(int, list(input().strip()))) for _ in range(N)]
    print(check(video, N))

'''
110 / 0101 / 0010 / 1 / 0001
'''