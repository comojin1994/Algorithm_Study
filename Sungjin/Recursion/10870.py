import sys
input = sys.stdin.readline

fibo = {0: 0, 1: 1, 2: 1}

def fibonaci(n):
	if n in fibo.keys():
		return fibo[n]
	fibo[n] = fibonaci(n-1) + fibonaci(n-2)
	return fibo[n]

n = int(input())
print(fibonaci(n))