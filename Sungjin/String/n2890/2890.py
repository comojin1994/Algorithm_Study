import sys
input = sys.stdin.readline

if __name__ == '__main__':
    R, C = map(int, input().strip().split())
    ka = [list(input().strip())[1:-1] for _ in range(R)]
    result = [[i+1,0] for i in range(9)]
    for line in ka:
        cnt = 0
        for check in line:
            if check == '.': cnt += 1
            else:
                result[int(check)-1][1] = cnt
    result = sorted(result, key=lambda x: x[1], reverse=True)
    ans = [0 for i in range(9)]
    rank = 1
    for i in range(8):
        if result[i][1] != result[i+1][1]:
            ans[result[i][0]-1] = rank
            rank += 1
        else:
            ans[result[i][0] - 1] = rank
    ans[result[-1][0] - 1] = rank
    for r in ans: print(r)


'''
11 13
S........111F
S.......222.F
S......333..F
S.....444...F
S....555....F
S...666.....F
S...........F
S..777......F
S.888.......F
S...........F
S999........F

10 10
S.....111F
S....222.F
S...333..F
S..444...F
S.555....F
S666.....F
S.777....F
S..888...F
S........F
S...999..F
'''