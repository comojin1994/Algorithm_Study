import sys

input = sys.stdin.readline

N = int(input())

c = 0
c_list = [10000]

def main(N, c, c_set):
    # print('number : %d, count : %d, c_set : %s' % (N,c,c_list))
    if c > c_list[0]:
        return c_list
    if N == 1:
        if c_list[0] > c: c_list[0] = c
        return c_list
    if N % 3 == 0:
        main(int(N/3), c+1, c_list)
    if N % 2 == 0:
        main(int(N/2), c+1, c_list)
    main(N-1, c+1, c_list)

main(N,c,c_list)
print(c_list[0])