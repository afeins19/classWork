"""Assignment-3 (30 points)
Recursive Functions Due date: 1 week
Exercise-1: (7.5 points)
Write a recursive Python function that has a parameter representing a list of integers and returns
the maximum stored in the list. Thinking recursively, the maximum is either the first value in the
list or the maximum of the rest of the list, whichever is larger. If the list only has 1 integer, then
its maximum is this single value, naturally. Copy and paste the screenshot of the result.

Exercise-2: (7.5 points)
Run the Recursive Fibonacci function defined in the class notes with input a) 50 and b) 115. Copy
and paste the screenshot of the result. Explain your understanding about this recursive function
and the iterative function which you have written for your earlier assignment.
Note: If the program doesn’t work, test it with lesser values (let’s say 10 or 15) and record your
observations.

Exercise-3: (7.5 points)
Write a recursive function to calculate the sum of the positive integers of n+(n-2)+(n-4)...
Copy and paste the screenshot of the result.

Exercise-4: (7.5 points)
Write a recursive function to calculate the value of 'a' to the power 'b'? Copy and paste the
screenshot of the result.
"""
import CommandLineTools as clt

"Exercise 1"
def recursive_max(vals: list):
    if len(vals) == 1:
        return vals[0]
    else:
        smallest = min(vals[0], vals[1])
        vals.remove(smallest)
        return recursive_max(vals)

"Exercise 2"
def recursive_fibonacci(val: int):
    if val < 2:
        return val
    else:
        return recursive_fibonacci(val-2) + recursive_fibonacci(val-1)   #recursive call
        #fib(4) = fib(3) + fib(2) = (fib(2)+fib(1)) + (fib(1)+fib(0)) = (2 + 1) + (1 + 0) = 3+1=4


"Exercise 3"
def recursive_sum(n: int, subtract: int = 0):
    if n<1:
        return 0
    else:
        return n + recursive_sum(n-subtract, subtract+2)


"Exercise 4"
def recursive_power(a: int, pow: int):
    if pow == 0:
        return 1
    else:
        return a * recursive_power(a, pow-1)

clt.header("Maxmimum")
print(recursive_max([1,55,23429,123,523,42]))

clt.header("Fibonacci")
print(recursive_fibonacci(36))
print(recursive_fibonacci(10))


clt.header("Sum")
print(recursive_sum(55))

clt.header("power")
print(recursive_power(2,5))
