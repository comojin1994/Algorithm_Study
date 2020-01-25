import sys
input = sys.stdin.readline

loop = int(input())

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        return self.stack
    def pop(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack[-1])
            self.stack.pop(-1)
    def size(self):
        print(len(self.stack))
    def empty(self):
        if len(self.stack) == 0:
            print(1)
        else:
            print(0)
    def top(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack[-1])

ans = Stack()
for _ in range(loop):
    order = input().strip().split(' ')
    if order[0] == 'push':
        ans.push(order[1])
    elif order[0] == 'pop':
        ans.pop()
    elif order[0] =='size':
        ans.size()
    elif order[0] == 'empty':
        ans.empty()
    elif order[0] == 'top':
        ans.top()
    else:
        print('Input Error')
