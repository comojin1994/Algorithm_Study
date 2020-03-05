# merge sort algorithm
# n//2로 divide
# 1개씩의 요소가 남기까지 재귀적으로 conquer
# 2개씩 반복적으로 merge


def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2;
    left = merge_sort(L[mid:])
    right = merge_sort(L[:mid])
    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    L = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L.append(left[i])
            i += 1
        else:
            L.append(right(j))
            j += 1

    while i < len(left):
        L.append(left[i])
        i += 1
    while j < len(right):
        L.append(right[j])
        j += 1

    return L


if __name__ == "__main__":
    n = int(input())
    L = [int(input()) for _ in range(n)]
    for i in merge_sort(L):
        print(i)
