import sys
input = sys.stdin.readline

def recursive(skill, link_list, answer):
    if skill not in link_list.keys():
        print(' '.join(answer))
        return -1
    else:
        for next_skill in link_list[skill]:
            answer.append(next_skill)
            recursive(next_skill, link_list, answer)
            answer.pop()



def main(skill_list, N, link_list):
    answer = []
    linked_skill_list = []
    for skill in skill_list:
        if skill not in link_list.keys(): continue
        if skill in linked_skill_list: continue
        answer.append(skill)
        recursive(skill, link_list, answer)
        answer.pop()
        linked_skill_list += link_list[skill]



if __name__ == '__main__':
    skill_list = list(input().strip().split())
    N = int(input())
    link_list = {}
    for _ in range(N):
        start, end = list(input().strip().split())
        if start in link_list.keys():
            link_list[start].append(end)
        else:
            link_list[start] = [end]
    main(skill_list, N, link_list)

'''
h g f w r
4
h g
h f
g r
g w
'''