import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, idx = map(int, input().strip().split())
        seq_ = deque(map(int, input().strip().split()))
        seq = deque()
        for i in range(N):
            seq.append([seq_[i], i])
        cnt = 0; n = -1
        while seq_:
            if seq_[0] == max(seq_):
                seq_.popleft()
                _, n = seq.popleft()
                cnt += 1
            else:
                temp_ = seq_.popleft()
                temp = seq.popleft()
                seq_.append(temp_)
                seq.append(temp)
            if n == idx:
                print(cnt)
                break
