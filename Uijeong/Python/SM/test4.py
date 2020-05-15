import sys
input = sys.stdin.readline

def binary_search(arr, key):
    lower = 0
    upper = len(arr) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if key <= arr[mid]:
            upper = mid - 1
        else:
            lower = mid + 1
    return lower

if __name__ == "__main__":
    N = int(input())
    skills = {}
    for i in range(N):
        skills[i] = list(map(int, input().strip().split()))
    skills_sort = sorted(skills.items(), key=lambda x: [x[1][0], x[1][1]])
    e_sort = [skills_sort[0][1][1]]
    for key, value in skills_sort[1:]:
        idx = binary_search(e_sort, value[0])
        skills[key] = idx
        idx = binary_search(e_sort, value[1])
        e_sort = e_sort[:idx] + [value[1]] + e_sort[idx:]
    skills = sorted(skills.keys())
    for sk in skills:
        print(sk)
