def next_position(left, i, j):
    direction = { 'R': 0, 'D': 1, 'L': 2, 'U': 3 }
    if left == direction['D']:
        return i + 1, j
    elif left == direction['R']:
        return i, j + 1
    elif left == direction['U']:
        return i - 1, j
    elif left == direction['L']:
        return i, j - 1


def solution(maze):
    answer = 0
    finish = len(maze) - 1
    i, j = 0, 0 # position
    direction = { 'R': 0, 'D': 1, 'L': 2, 'U': 3 }
    current = direction['D']
    left = current - 1
    while i != finish or j != finish:
        next_i, next_j = next_position(left, i, j)
        if next_i > finish or next_i < 0 or next_j > finish or next_j < 0 or maze[next_i][next_j] == 1:
            current = (current + 1) % 4
            left = current - 1 if current > 0 else 3
            continue
        i, j = next_i, next_j
        current = left
        left = current - 1 if current > 0 else 3
        answer += 1
    return answer


if __name__ == '__main__':
    mazes = [[[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]],
             [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]],
             [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]],
             [[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]]

    for maze in mazes:
        solution(maze)
        break