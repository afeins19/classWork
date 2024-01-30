"""Recursion Functions:
    Heuristic: if a problem can be broken down into smaller identical pieces, recursion may be used to solve a problem
    (apart from being an elegant solution, some functions may only be solved recursively)

Laws Of Recursion:
    1. base case (terminating condition)
    2. function must change states and move towards the base case
    3. recursive call (function calls itself)

Types of Recursive Functions:

    Direct Recursive: simply a function that calls itself

    Indirect Recursive: A calls B and B calls A

    Mutually Recursive: A chain of calls which terminates back at base case
"""

"Iterative (Non-recursive) Function:"
def iterative_sum(vals: list):
    out = 0
    for val in vals:
        out += val
    return out

"Recursive Functions:"
def recursive_sum(vals: list):
    if len(vals) == 1:  #terminating condition
        return vals[0]
    else:
        return vals[0] + recursive_sum(vals[1:])    #recursive call

def recursive_factorial(val: int):
    if val == 0: #base case
        return 1
    else:
        return val * recursive_factorial(val-1)  #recursive call

def recursive_fibonacci(val: int):
    if val < 2:
        return val
    else:
        return recursive_fibonacci(val-2) + recursive_fibonacci(val-1)   #recursive call
        #fib(4) = fib(3) + fib(2) = (fib(2)+fib(1)) + (fib(1)+fib(0)) = (2 + 1) + (1 + 0) = 3+1=4

def recursive_reverse(items: []):
    if not items:
        return []

    return  [items[-1]]+ recursive_reverse(items[:-1])

#print(iterative_sum([1,2,3,4,5]))

print(recursive_sum([1,2,3,4,5]))
#print(recursive_fibonacci(36))
#print(recursive_factorial(9))
print(recursive_reverse([1,2,3,4,5]))




