import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())

    # 최빈값 -> 계수정렬
    C = [0] * 8001
    L = []
    for i in range(n):
        m = int(input())
        L.append(m)
        C[m] += 1

    i, maxC, maxCnt = 0, max(C), 0
    for j in range(-4000, 4001):
        if C[j] > 0:
            for _ in range(C[j]):
                L[i], i = j, i + 1
            if maxCnt < 2 and maxC == C[j]:
                maxCntNum, maxCnt = j, maxCnt + 1

    print(round(sum(L)/n))
    print(L[n//2])
    print(maxCntNum)
    print(max(L)-min(L))