import sys
input = sys.stdin.readline

if __name__ == '__main__':
    seq1 = [0] + list(input().strip())
    seq2 = [0] + list(input().strip())
    dp = [[0]*len(seq1) for _ in range(len(seq2))]

    for i in range(1, len(seq2)):
        for j in range(1, len(seq1)):
            if seq2[i] == seq1[j]:
                dp[i][j] += dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    print(max(dp[-1]))