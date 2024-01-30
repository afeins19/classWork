#this folder will use a stack data type to balance the parentheses of some expression
'''Why stacks are a good data structure for this technique:
-------------------------------------------------------------------------------------
In an expression, as you process symbols from left to right, the closing symbols must be matched
with the most recent opening symbols (the newest opening symbols are the first to be matched with
the next found closing symbol)...sounds stacky
'''
from Data_Structures.Stacks.Stack_Implement import Stack
import re

#returns True if parantheses are balanced
def isBalanced(expression):
    expBalanced=True
    parStack = Stack()

    #scanning through list of all parenth.
    for i in list(expression):
        #if '(' add it to stack
        if i=='(':
            parStack.push(i)

        #a ) must have a matching ( so i there is not one in the stack...
        #...that means the exp is notbalanced
        if i==')':
            if parStack.isEmpty()==True:
                expBalanced=False
                break
            else:
                parStack.pop()
    return expBalanced


print(isBalanced('())'))