from itertools import combinations


def lcs(a, b):
    lcs = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    len_lcs = lcs[-1][-1]

    seq = ''
    if len_lcs > 1:
        i, j = len(a), len(b)
        cnt = len_lcs
        while i != 0 and j != 0:
            if lcs[i - 1][j] == cnt:
                i = i - 1
            elif lcs[i][j - 1] == cnt:
                j = j - 1
            elif lcs[i - 1][j - 1] == cnt - 1:
                cnt -= 1
                seq += a[i - 1]
                i, j = i - 1, j - 1

    return len_lcs, seq[::-1]


def solution(orders, course):
    answer = []
    orders = [sorted(order) for order in orders]
    d = {}

    for i, order in enumerate(orders):
        for j, compare in enumerate(orders[i + 1:]):
            len_lcs, seq = lcs(order, compare)

            for k in course:
                for cb in combinations(seq, k):
                    cb = ''.join(cb)
                    d[cb] = d[cb] + 1 if cb in d else 1
    len_dict = {}
    for k in course:
        len_dict[k] = []
        max_k = 0
        for key, values in d.items():
            if len(key) == k and max_k <= values:
                if max_k < values:
                    len_dict[k] = [key]
                    max_k = values
                else:
                    len_dict[k].append(key)

    answer = sum(list(len_dict.values()), [])
    answer = sorted(answer)

    return answer