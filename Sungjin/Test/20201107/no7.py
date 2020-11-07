def solution(n, horizontal):

    answer = [[0 for i in range(n)] for j in range(n)]

    i = 0
    j = 0
    direction = ''
    check = 0
    for k in range(n*n-1):
        if k == 0:
            if horizontal == True:
                j += 1
                direction = "L"
            else:
                i += 1
                direction = "R"

            answer[i][j] = 1

        else:
            if check != n-1:
                if direction == 'L':
                    answer[i+1][j-1] = answer[i][j] + 2
                    i += 1
                    j -= 1
                    if j == 0:
                        direction = "D"
                elif direction == "R":
                    answer[i-1][j+1] = answer[i][j] + 2
                    i -= 1
                    j += 1
                    if i == 0:
                        direction = "U"
                elif direction == "D":
                    answer[i+1][j] = answer[i][j] + 1
                    i += 1
                    direction = "R"
                else:
                    answer[i][j+1] = answer[i][j] + 1
                    j += 1
                    direction = "L"

                if i == n-1 or j == n-1:
                    check = max(i, j)
            else:
                if direction == 'L':
                    answer[i+1][j-1] = answer[i][j] + 2
                    i += 1
                    j -= 1
                    if i == n-1:
                        direction = "D"
                elif direction == "R":
                    answer[i-1][j+1] = answer[i][j] + 2
                    i -= 1
                    j += 1
                    if j == n-1:
                        direction = "U"
                elif direction == "D":
                    answer[i][j+1] = answer[i][j] + 1
                    j += 1
                    direction = "R"
                else:
                    answer[i+1][j] = answer[i][j] + 1
                    i += 1
                    direction = "L"

    return answer