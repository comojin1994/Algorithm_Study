import sys
input = sys.stdin.readline

N = int(input())
words = list(set(input().strip() for _ in range(N)))
words = sorted(words)
words = sorted(words, key=lambda x: len(x))
for w in words:
    print(w)