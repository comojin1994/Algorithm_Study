import sys
input = sys.stdin.readline

def cal_score(team, ene):
    st, se = 0, 0
    for i in range(N//2):
        for j in range(i, N//2):
            st += abil[team[i]-1][team[j]-1] + abil[team[j]-1][team[i]-1]
            se += abil[ene[i]-1][ene[j]-1] + abil[ene[j]-1][ene[i]-1]
    return abs(st - se)

def func(idx, N, j):
    global result
    if idx == N//2:
        team = [i+1 for i, p in enumerate(nums) if p]
        ene = [i+1 for i, p in enumerate(nums) if not p]
        temp = cal_score(team, ene)
        result = min(result, temp)
        if result == 0:
            print(result)
            sys.exit(0)
        return 1

    for i in range(j, N):
        if nums[i]:
            continue
        nums[i] = True
        func(idx+1, N, i)
        nums[i] = False

if __name__ == '__main__':
    N = int(input())
    nums = [False for _ in range(N)]
    abil = []
    for _ in range(N):
        abil.append(list(map(int, input().strip().split())))
    result = 100000
    func(0, N, 0)
    print(result)