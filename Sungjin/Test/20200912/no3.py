import sys
import copy
input = sys.stdin.readline

def get_intersection(ele):
    return (ele[0].intersection(ele[1]).intersection(ele[2])).intersection(ele[3])

def main(info, query):
    # 데이터
    info = [ele.split(' ') for ele in info]
    info = list(zip(*info))

    # 쿼리
    query = [ele.replace(' and ', ' ').split(' ') for ele in query]
    query = list(zip(*query))

    answer = [0] * len(query[0])
    idx_answer = [[set(i for i in range(len(info[0])))] * len(query[0])] * 4

    # query col
    past = list()

    for i, ele in enumerate(info):
        if i == 4:
            for idx, ele_ in enumerate(zip(*past, query[i])):
                for score_idx in get_intersection(ele_[:-1]):
                    if int(ele[score_idx]) >= int(ele_[-1]):
                        answer[idx] += 1

        else:
            for j, q in enumerate(query[i]):
                if q != '-':
                    idx_answer[i][j] = set([i for i, e in enumerate(info[i]) if e == q])
            past.append(copy.deepcopy(idx_answer[i]))

    return answer

if __name__ == '__main__':
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    main(info, query)