import sys
input = sys.stdin.readline

if __name__ == '__main__':
    S = list(input().strip())
    dic = dict()
    odd = 0
    for s in S:
        if s in dic.keys(): dic[s] += 1
        else: dic[s] = 1
    even, odd = [], []
    for s, v in dic.items():
        if v % 2 == 0: even.append(s)
        else: odd.append(s)
    if len(odd) > 1: print("I'm Sorry Hansoo"); sys.exit(0)

    even = sorted(even)
    result = ''
    for s in even:
        result += s * (dic[s]//2)
    if len(odd) == 1: result += odd[0] * dic[odd[0]]
    for s in reversed(even):
        result += s * (dic[s]//2)
    print(result)