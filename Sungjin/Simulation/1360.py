import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    Ord = [list(input().strip().split()) + [True] for _ in range(N)]
    # type a 1 True //  undo 3 5 True
    result = ''
    for i in range(N - 1, -1, -1):
        if Ord[i][0] == 'undo' and Ord[i][-1]:
            idx = int(Ord[i][2]) - int(Ord[i][1])
            j = i - 1
            while j >= 0:
                if int(Ord[j][2]) < idx: break
                if Ord[j][0] == 'undo':
                    Ord[j][-1] = not Ord[j][-1]
                j -= 1
    for i in range(N - 1, -1, -1):
        if Ord[i][0] == 'undo' and Ord[i][-1]:
            idx = int(Ord[i][2]) - int(Ord[i][1])
            j = i - 1
            while j >= 0:
                if int(Ord[j][2]) < idx: break
                if Ord[j][0] == 'type':
                    Ord[j][-1] = not Ord[j][-1]
                j -= 1
    for li in Ord:
        if li[0] == 'type' and li[-1]: result += li[1]
    print(result)

'''
4
type a 1
type b 2
undo 2 3
undo 2 4

5
type a 1
type b 2
undo 2 3
undo 2 4
undo 2 5

5
type a 1
type b 2
undo 2 3
undo 2 4
undo 2 6

6
type a 1
type b 2
undo 2 3
undo 2 4
type c 5
undo 2 6
'''