from collections import deque

def solution(boxes):
    answer = 0
    box_count = len(boxes)
    allbox = []
    for box in boxes:
        allbox += box
    elements = set(allbox)
    number_of_ele = dict()
    for ele in elements:
        number_of_ele[ele] = allbox.count(ele)

    items = deque(sorted(number_of_ele.items(), key=lambda x: x[1], reverse=True))
    current_box = 0
    while box_count != current_box:
        if max(list(items), key=lambda x: x[1])[1] == 1:
            current_box += 1
            answer += 1
        else:
            node = items.popleft()
            if node[1] >= 2:
                q = node[1] // 2
                r = node[1] % 2

                current_box += q
                node = (node[0] ,r)
            if node[1] != 0:
                items.append(node)
    return answer

if __name__ == '__main__':
    boxess = [[[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]],
              [[1, 2], [3, 4], [5, 6]],
              [[1, 2], [2, 3], [3, 1]]]
    for boxes in boxess:
        print(solution(boxes))