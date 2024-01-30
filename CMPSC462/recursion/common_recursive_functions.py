"""These are implementations of recursive problems"""

#Recursive Factorial
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


#Exercise 4: Python program to find the sum of natural numbers up to n using recursive function

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)

#Exercise 5: Write a Python program to calculate the sum of a list of numbers
def recursive_sum_list(vals: list):
    if not vals:
        return 0
    else:
        return vals[0] + recursive_sum_list(vals[1:])

#Exercise 6: Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
def recursive_sum_minus_two(n):
    if n < 2:
        return n
    else:
        return n + recursive_sum_minus_two(n-2)

#Exercise 7: Write a recursive Python program to print a list in reverse natural order.
def reverse_list(vals: list):
    if not vals:
        return
    else:
        print(vals[-1])
        return reverse_list(vals[:-1])

#Exercise 8: Write a Python program to calculate the value of 'a' to the power 'b'.

def recursive_pow(a,b):
    if b == 0:
        return 1
    else:
        return a * recursive_pow(a,b-1)


