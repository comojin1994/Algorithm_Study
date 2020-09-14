import sys
input = sys.stdin.readline

def solution():
    num_li = {0:'0'}
    words = [list(input().strip()) for _ in range(int(input()))]
    words = sorted(words, key=lambda x: len(x), reverse=True)
    for idx, word in enumerate(words):
        words[idx] = [0] * (8 - len(word)) + word

    cnt = 9
    for alpha in zip(*words):
        for w in alpha:
            if w == 0: continue
            if w not in num_li.keys():
                num_li[w] = str(cnt)
                cnt -= 1

    result = 0
    for i, word in enumerate(words):
        for j, w in enumerate(word):
            words[i][j] = num_li[w]
        result += int(''.join(words[i]))

    return result

if __name__ == '__main__':
    print(solution())