result = []

def recursive(n, size):
    global result
    n = list(str(n))
    if len(n) == 1:
        a = size
        b = int(n[0])
        result.append([a, b])
        return 1
    else:
        for i in range(1, len(n)):
            n1 = int(''.join(n[:i]))
            n2 = int(''.join(n[i:]))
            if len(n[:i]) != len(str(n1)): continue
            if len(n[i:]) != len(str(n2)): continue
            newn =  n1 + n2
            recursive(newn, size + 1)

def solution(n):
    global result
    size = 0
    recursive(n, size)
    return min(result, key=lambda x: x[0])

if __name__ == '__main__':
    print(solution(73425))