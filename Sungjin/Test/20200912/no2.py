import sys
from itertools import combinations
input = sys.stdin.readline

def lcs(string_1, string_2):
    dp = [[""] * (len(string_2) + 1) for _ in range(len(string_1) + 1)]
    for i in range(1, len(string_1) + 1):
        for j in range(1, len(string_2) + 1):
            if string_1[i - 1] == string_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + string_1[i - 1]
            else:
                if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    if len(dp[-1][-1]) == 0:
        return 0
    else:
        return dp[-1][-1]

def main(orders, course):
    answer = []
    orders = [sorted(order) for order in orders]
    result = {}

    for i, string_1 in enumerate(orders):
        for string_2 in orders[i + 1:]:
            lcs_result = lcs(string_1, string_2)

            for c in course:
                if lcs_result != 0:
                    for step in combinations(lcs_result, c):
                        step = ''.join(step)
                        if step not in result.keys(): result[step] = 1
                        else: result[step] += 1

    result_2 = {}
    for c in course:
        result_2[c] = []
        max_ = 0
        for key, values in result.items():
            if len(key) == c and max_ <= values:
                if max_ < values: result_2[c] = [key]; max_ = values
                else: result_2[c].append(key)

    answer = sum(list(result_2.values()), [])
    answer = sorted(answer)
    print(answer)

if __name__ == '__main__':
    orderss = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
               ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
               ["XYZ", "XWY", "WXA"]]
    courses = [[2,3,4], [2,3,5], [2,3,4]]

    for orders, course in zip(orderss, courses):
        main(orders, course)
        print("="*30)
        # break