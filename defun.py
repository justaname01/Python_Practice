#practicing basic functions

def fibo(n):
	result = []
	a,b = 0,1
	while(a < n):
		result.append(a)
		a,b = b, a + b
	return result

	

print(fibo(10))
print(fibo(20))
print(fibo(50))
print(fibo(100))
