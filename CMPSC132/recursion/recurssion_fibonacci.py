#SAVE AS .py PLZ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Example of Recursion & Memoization in Python 
#this example will construct the fibonaccii sequence 
'''
Fibonacci Sequence: a sequence with the first two terms being 0,1 and the (n+1)th term 
is the (n-2)cond term +(n-1)st term 
''' 
#output should be: [1,1,2,3,5,8,13,21,...,] 
#-------------------------------------------------------------------------------------
stop_at=int(input('\nPlease Indicate Stop Value: '))  

#memoization-caching previous values to avoid 
#redundant calculations 
fibonacci_cache={}

def fibonacci(n): 
	#check if value is cahced, then return it 
	if n in fibonacci_cache: 
		return fibonacci_cache[n]
	if n==1: 
		return 1
	if n==2: 
		return 1 
	elif n>2 :
		value =  fibonacci(n-1) + fibonacci(n-2) 
	fibonacci_cache[n]=value 
	return value

for n in range(1,stop_at+1) : 
	print(str(n)+': '+str(fibonacci(n))) 

 
