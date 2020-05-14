def solution(numbers, hand):
    answer = ''
    point = [[3, 1]] + [[i//3, i%3] for i in range(9)] + [[3,0], [3, 2]]
    right, left = 11, 10
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = n
        elif n in [3, 6, 9]:
            answer += 'R'
            right = n
        else:
            dis_r = (point[n][0] - point[right][0])**2 + (point[n][1] - point[right][1])**2
            dis_l = (point[n][0] - point[left][0])**2 + (point[n][1] - point[left][1])**2
            if dis_r > dis_l:
                left = n
                answer += 'L'
            elif dis_r < dis_l:
                right = n
                answer += 'R'
            else:
                if hand == 'right':
                    right = n
                    answer += 'R'
                else:
                    left = n
                    answer += 'L'
    return answer

if __name__ == "__main__":
    print(solution([1,5,0,1,1,0,1], 'right'))