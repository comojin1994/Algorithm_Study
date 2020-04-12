import sys
input = sys.stdin.readline

def mult(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A
    elif B % 2 == 1:
        return mult(A, B - 1, C) * A
    else:
        return (mult(A, B // 2, C) ** 2) % C

if __name__ == '__main__':
    A, B, C = map(int, input().strip().split())
    print(mult(A, B, C) % C)