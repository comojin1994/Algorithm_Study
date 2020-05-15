import sys
input = sys.stdin.readline

if __name__ == "__main__":
    L = [3,1,6,2,7,30,1]
    L.sort()
    dp = [0] * len(L)
    dp[0] = L[0]
    print(L)
    for i in range(1, len(L)):
        if L[i] <= dp[i - 1]:
            dp[i] = L[i] + dp[i - 1]
        else:
            print(dp)
            print(dp[i-1])
            break
    print(dp[-1] + 1)




