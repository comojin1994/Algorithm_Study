import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
cards = list(map(int, input().strip().split()))
value = 0
breakvalue = False

for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            temp = cards[i] + cards[j] + cards[k]
            if temp > value and temp <= M:
                value = temp
            if value == M:
                breakvalue = True
                break
        if breakvalue:
            break
    if breakvalue:
        break
print(value)