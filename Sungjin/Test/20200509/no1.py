import sys
input = sys.stdin.readline

def calDist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

if __name__ == '__main__':
    numbers = list(map(int, input().strip().split()))
    hand = input().strip()
    cord = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2]]
    result = ''
    n_L = 10
    n_R = 11
    for o in numbers:
        if o in [1, 4, 7]: result += 'L'; n_L = o
        elif o in [3, 6, 9]: result += 'R'; n_R = o
        else:
            dist_L = calDist(cord[o], cord[n_L])
            dist_R = calDist(cord[o], cord[n_R])
            if dist_R > dist_L: result += 'L'; n_L = o
            elif dist_R < dist_L: result += 'R'; n_R = o
            else:
                if hand == 'right': result += 'R'; n_R = o
                else: result += 'L'; n_L = o
    print(result)

'''
1 3 4 5 8 2 1 4 5 9 5
right

7 0 8 2 8 3 1 5 7 6 2
left

1 2 3 4 5 6 7 8 9 0
right
'''