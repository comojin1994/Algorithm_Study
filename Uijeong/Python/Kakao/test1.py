import sys
import re
input = sys.stdin.readline

def getPrior(search):
    global d
    for i, op in enumerate(search):
        d[op] = i
    return d

def dfs(k):
    global search, max
    if k == 3:
        dict = getPrior(search)
        result = abs(int(calculate(dict)))
        if max < result:
            max = result
        return
    for key in d.keys():
        if key in search: continue
        search.append(key)
        dfs(k+1)
        search = search[:-1]

def calculate(dict):
    global expression
    s1, s2 = [], []
    operand = ''
    for i, s in enumerate(expression):
        if s in ['+', '-', '*']:
            s1.append(operand)
            if len(s2) == 0:
                s2.append(s)
            else:
                if dict[s2[-1]] < dict[s]:
                    temp = s2.pop() + s1.pop()
                    temp = s1.pop() + temp
                    s1.append(str(eval(temp)))
                while len(s2) > 0:
                    if dict[s2[-1]] == dict[s]:
                        temp = s2.pop() + s1.pop()
                        temp = s1.pop() + temp
                        s1.append(str(eval(temp)))
                    else: break
                s2.append(s)
            operand = ''
        elif i == len(expression) - 1:
            operand += s
            s1.append(operand)
        else:
            operand += s

    while len(s2) != 0:
        temp = s2.pop() + s1.pop()
        temp = s1.pop() + temp
        s1.append(str(eval(temp)))
    return s1[0]

if __name__ == "__main__":
    expression = input().strip()
    d = {'+': 0, '-': 0, '*': 0}
    operand = expression.replace('+', ',').replace('-', ',').replace('*',',').split(',')
    operator = [s for s in expression if s in ['+', '-', '*']]
    max = 0
    search = []
    dfs(0)
    print(max)