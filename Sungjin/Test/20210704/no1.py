import sys
input = sys.stdin.readline


def get_partial_word(word):
    word = sorted(word)
    word = ''.join(word)
    return word


def solution(S, pattern):
    answer = 0

    pattern = get_partial_word(pattern)
    for i in range(len(S) - len(pattern) + 1):
        partial_word = get_partial_word(S[i:i + len(pattern)])
        if pattern == partial_word:
            answer += 1

    return answer


if __name__ == '__main__':
    S = input().strip()
    pattern = input().strip()
    print(solution(S, pattern))


'''
tegsornamwaresomran
ransom

'''