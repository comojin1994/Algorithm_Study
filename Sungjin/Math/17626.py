import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    s1 = set((i+1)**2 for i in range(223))
    s2, s3 = set(), set()
    for i in s1:
        for j in s1:
            if i + j > 50000: break
            s2.add(i+j)
            for k in s1:
                if i + j + k > 50000: break
                s3.add(i + j + k)

    if n in s1: print(1)
    elif n in s2: print(2)
    elif n in s3: print(3)
    else: print(4)