import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        if current_node in graph.keys():
            for adjacent, weight in graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(queue, [distance, adjacent])

    return distances

def get_graph(fares):
    result = dict()
    for f in fares:
        if f[0] not in result.keys():
            result[f[0]] = dict()
            result[f[0]][f[1]] = f[2]
        else:
            result[f[0]][f[1]] = f[2]
        if f[1] not in result.keys():
            result[f[1]] = dict()
            result[f[1]][f[0]] = f[2]
        else:
            result[f[1]][f[0]] = f[2]
    return result


def main(n, s, a, b, fares):
    graph = get_graph(fares)
    first = dijkstra(graph, s)
    a1 = first[a] + first[b]
    a2_list = []
    for i in range(1, n+1):
        second = dijkstra(graph, i)
        if i in first.keys() and a in second.keys() and b in second.keys():
            a2_list.append(first[i] + second[a] + second[b])
    a2 = min(a2_list)
    return min(a1, a2)


if __name__ == '__main__':

    n = [6, 7, 6]
    s = [4, 3, 4]
    a = [6, 4, 5]
    b = [2, 1, 6]
    fares = [[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
             [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
             [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]]
    for n, s, a, b, fares in zip(n, s, a, b, fares):
        print(main(n, s, a, b, fares))