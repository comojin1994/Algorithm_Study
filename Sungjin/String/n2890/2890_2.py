import sys
input = sys.stdin.readline

if __name__ == '__main__':
    R, C = map(int, input().strip().split())
    ka = [list(input().strip())[1:-1] for _ in range(R)]
    result = [0 for _ in range(9)]
    rank = 1
    for li in zip(*ka):
        rank_check = False
        for x in li:
            if x != '.' and result[int(x)-1] == 0:
                result[int(x)-1] = rank
                rank_check = True
        if rank_check: rank += 1
    max_ = max(result) + 1
    result = [max_-r for r in result]
    for r in result:
        if r != max_: print(r)