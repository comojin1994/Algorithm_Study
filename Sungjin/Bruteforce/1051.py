import sys
input = sys.stdin.readline

def get_Corner(x, y, v):
    c1 = (x, y)
    c2 = (x, y+v-1)
    c3 = (x+v-1, y)
    c4 = (x+v-1, y+v-1)
    return c1, c2, c3, c4

def check_Same(c1, c2, c3, c4):
    if squ[c1[0]][c1[1]]==squ[c2[0]][c2[1]]==squ[c3[0]][c3[1]]==squ[c4[0]][c4[1]]: return True
    else: return False

def check(N, M, max_):
    while True:
        for i in range(N-max_+1):
            for j in range(M-max_+1):
                c1, c2, c3, c4 = get_Corner(i, j, max_)
                if check_Same(c1, c2, c3, c4): return max_**2
        max_ -= 1

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    squ = [list(input().strip()) for _ in range(N)]
    max_ = min(N, M)
    print(check(N, M, max_))