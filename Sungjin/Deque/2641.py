import sys
from collections import deque
input = sys.stdin.readline

def make_other(correct):
    temp = correct.popleft()
    correct.append(temp)
    return list(correct)

def change(correct):
    for i, c in enumerate(correct):
        if c == 1: correct[i] = 3
        elif c == 2: correct[i] = 4
        elif c == 3: correct[i] = 1
        else: correct[i] = 2
    return correct

def make_answer(correct):
    ans = []
    for _ in range(L):
        ans.append(make_other(correct))
    correct = reversed(correct)
    correct = deque(change(list(correct)))
    for _ in range(L):
        ans.append(make_other(correct))
    return ans

def print_result(res):
    print(len(res))
    for r in res:
        print(' '.join(map(str,r)))
    return 1

if __name__ == '__main__':
    L = int(input())
    correct = deque(map(int, input().strip().split()))
    N = int(input())
    test = [deque(map(int, input().strip().split())) for _ in range(N)]
    res = []
    ans = make_answer(correct)

    for t in test:
        t = list(t)
        if t in ans:
            res.append(t)
    print_result(res)