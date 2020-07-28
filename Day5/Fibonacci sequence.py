#Fibonacci sequence
def Fib(n):
	if n<0:
		print("Incorrect")
	elif n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return Fib(n-1) + Fib(n-2)

num = [1, 1]
for i in range(3, 21):
	num.append(Fib(i))

print(num)