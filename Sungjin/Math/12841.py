import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    C = list(map(int, input().strip().split()))
    L = list(map(int, input().strip().split()))
    R = list(map(int, input().strip().split()))
    diff = [R[i] - L[i] for i in range(n-1)]
    cumul = [0]
    for i in range(n-1):
        cumul += [cumul[i] + diff[n - 2 - i]]
        cumul[i] += C[n - 1 - i]
    cumul = cumul[::-1]
    min_v = min(cumul)
    place = cumul.index(min_v)
    result = sum(L[:place]) + C[place] + sum(R[place:])
    print(place + 1, result)


'''
1
2
0
0

4
1 1 1 1
10 20 30
1 1 1
'''