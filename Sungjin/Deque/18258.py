import sys
from collections import deque
input = sys.stdin.readline

class Que:
    def __init__(self):
        self.que = deque()
    def push(self, n):
        self.que.append(n)
        return n
    def pop(self):
        if self.empty() == 1: return -1
        else: return self.que.popleft()
    def size(self):
        return len(self.que)
    def empty(self):
        if len(self.que) == 0: return 1
        else: return 0
    def front(self):
        if self.empty() == 1: return -1
        else: return self.que[0]
    def back(self):
        if self.empty() == 1: return -1
        else: return self.que[-1]

def do(order, q):
    if len(order) == 2:
        q.push(order[1])
    elif order[0] == 'pop':
        print(q.pop())
    elif order[0] == 'size':
        print(q.size())
    elif order[0] == 'empty':
        print(q.empty())
    elif order[0] == 'front':
        print(q.front())
    elif order[0] == 'back':
        print(q.back())
    else:
        print('Error')
    return q

if __name__ == '__main__':
    N = int(input())
    q = Que()
    for _ in range(N):
        order = input().strip().split()
        q = do(order, q)