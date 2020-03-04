import sys
input = sys.stdin.readline

def check(room):
    result = 0
    for r in room:
        cnt = 0
        for s in r:
            if s == '.': cnt += 1
            if s == 'X':
                if cnt >= 2: result += 1
                cnt = 0
        if cnt >= 2: result += 1
    return result

if __name__ == '__main__':
    N = int(input())
    room = [input().strip() for _ in range(N)]
    row = check(room)
    col_ = list(zip(*room))
    col = check(col_)
    print(row, col)

'''
6
...X..
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
'''