import sys
input = sys.stdin.readline

if __name__ == '__main__':
    dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
           '9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    num16 = reversed(list(input().strip()))
    sum = 0
    for idx, n in enumerate(num16):
        sum += (16**idx)*dic[n]
    print(sum)
