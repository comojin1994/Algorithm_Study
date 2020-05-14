import sys
from collections import deque
input = sys.stdin.readline

def makeGraph(Rel):
    dict = {}
    for r in Rel:
        if r[0] in dict.keys(): dict[r[0]].add(r[1])
        else: dict[r[0]] = set(r)
    return dict

def bfs(Rel):
    Team = makeGraph(Rel)
    Teamlist = []
    for t in Team.keys():
        visited = []
        que = deque([t])
        while que:
            n = que.popleft()
            if n not in visited:
                visited.append(n)
                if n in Team.keys():
                    que += Team[n] - set(visited)
        Teamlist.append(visited)
    return Teamlist

def getValue(Teamlist):
    sum_ = 0
    for t in Teamlist:
        temp = []
        for i in t:
            temp.append(val[i-1])
        sum_t = 0
        for x in zip(*temp):
            sum_t += (max(x) - min(x)) * 2
        if sum_t > sum_: sum_ = sum_t
    return sum_

if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    val = [list(map(int, input().strip().split())) for _ in range(N)]
    Rel = sorted([sorted(list(map(int, input().strip().split()))) for _ in range(M)])
    Team = makeGraph(Rel)
    Teamlist = bfs(Rel)
    print(getValue(Teamlist))