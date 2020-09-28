from collections import deque

def solution(m, k):
    message, key = list(m), deque(list(k))
    for idx, m in enumerate(message):
        if len(key) == 0: break
        if m == key[0]:
            message[idx] = ''
            key.popleft()
    message = ''.join(message)
    return message


if __name__ == '__main__':
    ### INPUT ###
    ms = ["kkaxbycyz","acbbcdc"]
    ks = ['abc', 'abc']
    #############
    for m, k in zip(ms, ks):
        print(solution(m, k))