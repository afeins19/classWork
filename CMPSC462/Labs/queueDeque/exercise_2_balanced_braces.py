"""This Functionn will take in a series of encapsulating charecters and return
true if they are balanced
"""
from Labs import Stack

def is_balanced(val: str):
    s = Stack.Stack()

    # we will iterate over a list of chars in val
    for v in list(val):
        if v == "(":
            s.push(")")
        elif v == "[":
            s.push("]")
        elif v == "{":
            s.push("}")

        # check for right delimiters
        else:
            # if we have a right delimiter and the stack is empty...we have too many right delimiters
            if s.is_empty():
                return False

            elif s.pop() != v:
                return False

    #if we run through the loop and there are items in the stack...not enough right delimeters
    if not s.is_empty():
        return False

    return True

test = "[(])"
print(is_balanced(test))


