import sys
from itertools import product
input = sys.stdin.readline


def solution(word):
    word = tuple(word)

    dictionary = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, 6):
        words.extend(list(product(dictionary, repeat=i)))
    words = sorted(words)
    return words.index(word) + 1


if __name__ == '__main__':
    word = input().strip()

    print(solution(word))