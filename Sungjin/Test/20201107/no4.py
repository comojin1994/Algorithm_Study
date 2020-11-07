def findIndex(num, board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == num: return i, j


def getAllIndex(x, y, n):
    result = []
    ops = [[-n, -n], [-n, 0], [-n, n],
          [0, -n], [0, 0], [0, n],
          [n, -n], [n, 0], [n, n]]
    for op_x, op_y in ops:
        result.append([x + op_x, y + op_y])
    return result


def getDists(pt, indexes):
    result = []
    for index in indexes:
        dist = abs(pt[0] - index[0]) + abs(pt[1] - index[1])
        result.append(dist)
    return min(result)


def solution(n, board):
    answer = 0
    start = [0, 0]
    for i in range(1, (n ** 2) + 1):
        x, y = findIndex(i, board, n)
        indexes = getAllIndex(x, y, n)
        answer += getDists(start, indexes) + 1
        start = [x, y]
    return answer


if __name__ == '__main__':
    ns = [3, 2, 4, 2]
    board = [
        [[3, 5, 6], [9, 2, 7], [4, 1, 8]],
        [[2, 3], [4, 1]],
        [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]],
        [[1, 2], [3, 4]]
    ]
    for n, board in zip(ns, board):
        print(solution(n, board))