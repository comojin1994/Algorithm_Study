import sys
input = sys.stdin.readline

if __name__ == '__main__':
    S = list(input().strip())
    dic = dict()
    odd = 0
    for s in S:
        if s in dic.keys(): dic[s] += 1
        else: dic[s] = 1
    print(dic)
    half = ''
    odd_idx = -1
    items = list(dic.items())
    for idx, (alpha, cnt) in enumerate(sorted(items)):
        if cnt % 2 != 0:
            odd += 1
            if odd == 2: print("I'm Sorry Hansoo"); sys.exit(0)
            odd_idx = idx
        else:
            half += alpha * (cnt//2)
    half += items[odd_idx][0] * (items[odd_idx][1] // 2)
    result = half + items[odd_idx][0] + ''.join(reversed(list(half)))
    print(result)