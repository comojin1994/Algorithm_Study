import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        dict = {}
        for _ in range(n):
            value, key = input().strip().split()
            if key in dict.keys(): dict[key] += 1
            else: dict[key] = 1
        result = 1
        for n in list(dict.values()):
            result *= n+1
        print(result-1)
'''
1
6
hat headgear
sunglasses eyewear
turban headgear
mask face
sunglasses face
makeup face
'''