def add(a, b, op):
    a = int(a)
    b = int(b)
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    else:
        print('Error')


def solution(s, op):
    answer = []

    for i in range(1, len(s)):
        answer.append(add(s[0:i], s[i:len(s)], op))


if __name__ == '__main__':
    solution('1234', '+')