import sys

input = sys.stdin.readline

N = int(input())

loop = (N // 2) + 1 

fac_dict = {0: 1, 1: 1}
			
def factorial(n):
	if n in fac_dict.keys():
		return fac_dict[n]
	else:
		result = 1
		for i in range(1, n+1):
			result = result * i	
			fac_dict[i] = result
		return result		

def my_func(n, k):
	result = factorial(n-k) // (factorial(n-2*k) * factorial(k))
	return result

ans = 0
for i in range(loop):
	ans = ans + my_func(N, i)

print(ans % 10007)
