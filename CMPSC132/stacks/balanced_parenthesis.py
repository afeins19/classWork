from Stacks.stack_implement import Stack

def isBalanced(expression):
    s=Stack()
    for p in expression:
        if p == '(':
            s.push(p)
        if p == ')':
            if s.isEmpty():
                return False
            else:
                s.pop()
    if not s.isEmpty():
        return False
    return True

#check this one
check_list = ['((()))','(()()()())','(())','(()','))','(']
check_all = map(isBalanced,check_list)
print(list(check_all))