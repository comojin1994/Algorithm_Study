def calc(x, y, z):


    if x * y != 0:
        z = x - y
    elif y * z != 0:
        x = y + z
    elif x * z != 0:
        y = x - z

    return (x, y, z)

def solution(blocks):
    map_ = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    idx = 0
    for b in blocks:
        map_[idx][b[0]] = b[1]
        idx += 1
    max_floor = len(blocks)
    while True:
        for i in range(4):
            if i > max_floor: continue
            for j in range(5):
                if j > i: continue
                map_[i][j], map_[i+1][j], map_[i+1][j+1] = calc(map_[i][j], map_[i+1][j], map_[i+1][j+1])

        check = []
        for i in range(5):
            if i > max_floor: continue
            for j in range(5):
                if j > i: continue
                check.append(map_[i][j])

        temp = check[-max_floor:]
        flag = 1
        for t in temp:
            flag *= t
        if flag != 0: break
        print(check)
    return check

if __name__ == '__main__':
    ### INPUT ###
    blockss = [[[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]],
              [[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]]
    #############
    for blocks in blockss:
        solution(blocks)