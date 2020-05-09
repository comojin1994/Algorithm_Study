import sys
input = sys.stdin.readline

if __name__ == '__main__':
    gems = input().strip().split()
    l = len(gems)
    flag = 0
    for j in range(l):
        check = []
        DP = [0] * (l - j)
        for i in range(j, l):
            if gems[i] not in check:
                check.append(gems[i])
            DP[i - j] = len(check)
        max_ = DP.index(max(DP))
        print(DP, max_, check)
        print(j + 1, max_ + 1)

'''
DIA RUBY RUBY DIA DIA EMERALD SAPPHIRE DIA

AA AB AC AA AC

XYZ XYZ XYZ

ZZZ YYY NNNN YYY BBB
'''