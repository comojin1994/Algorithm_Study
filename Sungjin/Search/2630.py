import sys
input = sys.stdin.readline

def get_new(paper, x, y):
    new_paper = []
    for i in range(x[0], y[0]):
        new_paper.append(paper[i][x[1]:y[1]])
    return new_paper

def isall(paper):
    s = paper[0][0]
    for i in range(len(paper)):
        for j in range(len(paper)):
            if s != paper[i][j]:
                return False, s
    return True, s

def check(N, paper):
    global b, w
    tf, s = isall(paper)
    if tf:
        if s == 1: b += 1
        else: w += 1
        return 1
    else:
        check(N // 2, get_new(paper, (0, 0), (N // 2, N // 2)))
        check(N // 2, get_new(paper, (0, N // 2), (N // 2, N)))
        check(N // 2, get_new(paper, (N // 2, 0), (N, N // 2)))
        check(N // 2, get_new(paper, (N // 2, N // 2), (N, N)))

if __name__ == '__main__':
    N = int(input())
    paper = [list(map(int, input().strip().split())) for _ in range(N)]
    b, w = 0, 0
    check(N, paper)
    print('%d\n%d' % (w, b))