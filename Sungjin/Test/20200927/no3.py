
# node = {0: [[1, 2, 3], 0, 19], 1: [[4, 5], 1, 6]}
# {node: [[자식노드], floor, 연결개수]

def get_map(n, edges):
    output = dict()
    floor = [0] * n
    for edge in edges:
        if edge[0] not in output.keys():
            output[edge[0]] = [[]]
        floor[edge[1]] = floor[edge[0]] + 1
        output[edge[0]][0].append(edge[1])
    for idx, f in enumerate(floor):
        if idx not in output.keys():
            output[idx] = [[]]
        output[idx].append(f)
    return output

def count_child(node):
    nodes = list(reversed(list(node.items())))
    for n in nodes:
        if len(n[1][0]) == 0: node[n[0]].append(1)
        else:
            child = 0
            for value in n[1][0]:
                child += node[value][-1]
            node[n[0]].append(child + 1)
    return node

def get_current_node(floor, node):
    result = []
    for n in list(node.items()):
        if n[-1][1] == floor:
            result += n[-1][0]
    return result

def get_max_child(current, node):
    result = []
    for c in current:
        result.append((c, node[c]))
    if len(result) == 0: return -1
    return max(result, key=lambda x: x[-1][-1])

def del_child(max_child, node):
    del_li = max_child[-1][0]
    visited = [max_child[0]]
    while len(visited) < max_child[-1][-1]:
        for d in del_li:
            if d in visited: continue
            del_li += node[d][0]
            visited.append(d)
    for d in del_li:
        node.pop(d)
    node.pop(max_child[0])
    return node

def solution(n, edges):
    node = get_map(n, edges)
    node = count_child(node)
    node_item = list(node.items())
    max_floor = max([n[-1][-2] for n in node_item])
    floor = 0
    max_ = n
    while floor < max_floor:
        current = get_current_node(floor, node)
        max_child = get_max_child(current, node)
        if max_child == -1: break
        max_ -= max_child[-1][-1]
        node = del_child(max_child, node)
        floor += 1
        print(node)
    return max_


if __name__ == '__main__':
    ### INPUT ###
    ns = [19, 14, 10]
    edgess = [[[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]],
              [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]],
              [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]]]
    #############
    for n, edges in zip(ns, edgess):
        print(solution(n ,edges))