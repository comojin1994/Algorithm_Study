import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
chess = []
result = 10000
A = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
B = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

for _ in range(N):
    chess.append(input().strip())

def check(little, A):
    if len(little[0]) != 8:
        return 10000
    result = 0
    for i in range(8):
        for j in range(8):
            if little[i][j] != A[i][j]:
                result += 1
    return result

for i in range(N-7):
    for j in range(M-7):
        little = []
        for n in range(i, i+8):
            little.append(chess[n][j:j+8])
        temp = min(check(little, A), check(little, B))
        if temp < result:
            result = temp

print(result)