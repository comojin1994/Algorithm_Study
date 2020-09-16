import sys
input = sys.stdin.readline

def solution(hist):
    ans_1 = min(hist) * len(hist)
    past = hist[0]
    ans_2 = {0: past}

    idx = 0
    for i, h in enumerate(hist):
        if i == 0: continue
        if idx not in ans_2.keys():
            ans_2[idx] = h

        if past == h:
            ans_2[idx] += h
            past = h
        elif past < h:
            ans_2[idx] += past
        else:
            idx += 1
            past = h

    ans_22 = max(ans_2.items(), key=lambda x: x[1])

    return max(ans_1, ans_22[1])

if __name__ == '__main__':
    hist = [int(input()) for _ in range(int(input()))]
    print(solution(hist))