import sys
input = sys.stdin.readline

if __name__ == '__main__':
    angle = [int(input()) for _ in range(3)]
    if sum(angle) != 180: print('Error')
    elif len(set(angle)) == 3: print('Scalene')
    elif len(set(angle)) == 2: print('Isosceles')
    else: print('Equilateral')