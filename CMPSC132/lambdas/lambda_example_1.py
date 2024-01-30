#This program makes use of the lambda function 
# will print a number n and its square in format (n: n^2)
 
square=lambda x: x**2 

sqList=map(square,[i for i in range(100)]) 
for index in range(len(sqList)): 
	 print(str(index)+': '+str(sqList[index])) 
 
