import sys
input = sys.stdin.readline

if __name__ == '__main__':
    color = {'black': 0, 'brown': 1, 'red': 2,
             'orange': 3, 'yellow': 4, 'green': 5,
             'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    result = ''
    for _ in range(2):
        result += str(color[input().strip()])
    print(int(result) * (10 ** color[input().strip()]))