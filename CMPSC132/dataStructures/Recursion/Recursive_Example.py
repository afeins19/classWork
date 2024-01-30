'''Recursion is a method of solving problems that involves breaking a problem down
into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially.
Usually recursion involves a function calling itself. While it may not seem like much on the surface,
recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.'''

'''Recurssive algorithms consist of 3 main ideas: 
        1.) Base case (case for which the we break from the function)
        2.) The function will call itself 
        3.) The function should return values that move closer to the base case 
'''

#example factorial function
def factorial(n):
    #base case
    if n==1:
        return 1
    else:
        #recursive call
        out=n*factorial(n-1)
        return out


#example factorial but summing idk
def sum(i, n):
    if i == n:
        return 0
    else:
        return i + sum(i+1, n)


print(factorial(500))


