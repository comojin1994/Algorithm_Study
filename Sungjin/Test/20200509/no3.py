import sys
input = sys.stdin.readline

if __name__ == '__main__':
    gems = input().strip().split()
    l = len(gems)
    check = []
    DP = [0] * l
    for i in range(l):
        if gems[i] not in check:
            check.append(gems[i])
        DP[i] = len(check)
    max_ = DP.index(max(DP))

    check_ = []
    for i in range(max_, -1, -1):
        if gems[i] not in check_:
            check_.append(gems[i])
        if len(check_) == len(check): break

    print(i + 1, max_ + 1)

'''
DIA RUBY RUBY DIA DIA EMERALD SAPPHIRE DIA

AA AB AC AA AC

XYZ XYZ XYZ

ZZZ YYY NNNN YYY BBB
'''