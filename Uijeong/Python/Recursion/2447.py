
# 분할정복 + 재귀
# 문제의 규칙을 분할해서 찾기
def star(i, j):
    while i != 0:
        if i % 3 == 1 and j % 3 == 1:
            print(" ", end="")
            return
        i //= 3
        j //= 3
    print("*", end="")


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        for j in range(n):
            star(i, j)
        print()