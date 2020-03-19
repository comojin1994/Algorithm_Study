import sys
input = sys.stdin.readline

def check(li1, li2):
    if li1[0] < li2[0] and li1[1] < li2[1]: return True
    else: return False

if __name__ == '__main__':
    N = int(input())
    elec = [list(map(int, input().strip().split())) for _ in range(N)]
    elec = sorted(elec, key=lambda x: x[0])
    dp = [0 for _ in range(N)]

    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if elec[i][1] > elec[j][1] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print(N - max(dp))

    # for i in range(1, 101):
    #     if i == 100:
    #         print('%d %d' % (i, 1))
    #     else: print('%d %d' % (i, i+1))