from collections import deque

def solution(ball, order):
    result = []
    store = deque([])
    ball = deque(ball)
    order = deque(order)
    while len(order) + len(store) != 0:
        if len(store) != 0:
            past = 0
            while len(store) != past:
                past = len(store)
                for first_order in list(store):
                    # first_order = store.popleft()
                    if first_order == ball[0]:
                        result.append(ball.popleft())
                        store.remove(first_order)
                    elif first_order == ball[-1]:
                        result.append(ball.pop())
                        store.remove(first_order)


        if len(order) != 0:
            new_order = order.popleft()
            if new_order == ball[0]:
                result.append(ball.popleft())
            elif new_order == ball[-1]:
                result.append(ball.pop())
            else:
                store.append(new_order)
    return result


if __name__ == '__main__':
    balls = [[1, 2, 3, 4, 5, 6], [11, 2, 9, 13, 24]]
    orders = [[6, 2, 5, 1, 4, 3], [9, 2, 13, 24, 11]]

    for ball, order in zip(balls, orders):
        print(solution(ball, order))