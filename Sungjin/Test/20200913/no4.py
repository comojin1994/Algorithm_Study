# 오른쪽에 1이 있으면 아래로 한칸
# 왼쪽에 1이 있으면 위로 한칸
# 위쪽에 1이 있으면 오른쪽 한칸
# 아래에 1이 있으면 왼쪽 한칸

# 오른쪽을 짚고 가다가 없어지면 오른쪽 한칸
# 왼쪽을 짚고 가다가 없어지면 왼쪽 한칸
# 위쪽을 짚고 가다가 없어지면 위로 한칸
# 아래를 짚고 가다가 없어지면 아래로 한칸

# 지난번에 짚었던 벽의 위치
# 현재 벽의 위치
# 시간
from collections import deque

# 오, 아, 왼, 위
direction = [0, 1, 2, 3]

def next_step(wall, node):
    global direction
    if wall == direction[0]: return [node[0] + 1, node[1]]
    elif wall == direction[1]: return [node[0], node[1] + 1]
    elif wall == direction[2]: return [node[0] - 1, node[1]]
    elif wall == direction[3]: return [node[0], node[1] - 1]

def solution(maze):
    global direction
    answer = 0
    h = len(maze) - 1
    w = len(maze) - 1
    x, y = 0, 0  # position
    current = direction[1]
    left = current - 1
    while x != h or y != w:
        node = next_step(left, [x, y])
        if node[0] > h or node[0] < 0 or node[1] > w or node[1] < 0 or maze[node[0]][node[1]] == 1:
            current = (current + 1) % 4
            left = current - 1 if current > 0 else 3
            continue
        x, y = node[0], node[1]
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
        print(solution(maze))
        break