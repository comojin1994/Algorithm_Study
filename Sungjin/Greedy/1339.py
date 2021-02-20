import sys
input = sys.stdin.readline

def solution():
    num_li = {'0':'0'}
    result = []
    words = [list(input().strip()) for _ in range(int(input()))]
    words = sorted(words, key=lambda x: len(x), reverse=True)

    for idx, word in enumerate(words):
        words[idx] = ['0'] * (8 - len(word)) + word

    cnt = 9
    for word in zip(*words):
        for w in word:
            if w == '0': continue
            if w not in num_li.keys():
                num_li[w] = cnt
                cnt -= 1

    answer = 0
    for word in words:
        result = ''
        for w in word:
            result += str(num_li[w])
        answer += int(result)

    return answer

if __name__ == '__main__':
    print(solution())

'''    
6
ABABABAB
BABABABA
ABABABAB
BABABABA
CCCCCCCA
CCCCCCBA
'''