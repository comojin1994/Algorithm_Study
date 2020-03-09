import sys
input = sys.stdin.readline

if __name__ == '__main__':
    ham = [int(input()) for _ in range(3)]
    drink = [int(input()) for _ in range(2)]
    print(min(ham) + min(drink) - 50)