import sys
input = sys.stdin.readline


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']
alpha = sorted(alpha, reverse=True)


def get_last_letter(letters, start, i, k):
    search_space = letters[start: len(letters) - k + i + 1]
    for w in alpha:
        try:
            idx = search_space.index(w)
            return w, idx + start + 1
        except ValueError:
            continue


def solution(letters, k):
    answer = ''
    start = 0
    for i in range(k):
        w, start = get_last_letter(letters, start, i, k)
        answer += w
    return answer


if __name__ == '__main__':
    letters = input().strip()
    k = int(input().strip())

    print(solution(letters, k))


'''
zbgaj 3
'''