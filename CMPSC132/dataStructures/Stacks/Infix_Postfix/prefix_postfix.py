'''Infix --> Postfix --> Evaluated expression'''

from Data_Structures.Stacks.Stack_Implement import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
       #if the token has a '.' use float(token)
       #othersiwse use a int(token) in the next line  
        if token not in '()*-+/':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def postfixEval(postFixExpr):
    operandStack = Stack()
    tokenList = postFixExpr.split()

    for token in tokenList:
        if token not in ' +-*/':
            operandStack.push(int(token))
        else:
            op2 = operandStack.pop()
            op1 = operandStack.pop()
            result = do_math(token.op1,op2)
            operandStack.push(result)
        return operandStack.pop()


def do_math(op, val_1, val_2):
    if op =='*':
        return val_1 * val_2
    if op == '/':
        return val_2 / val_2
    if op == '+':
        return val_1 + val_2
    if op == '-':
        return val_1 - val_2


expression = '( 0 + 1 ) * ( 1 - 5 )'
print(postfixEval(infixToPostfix(expression)))