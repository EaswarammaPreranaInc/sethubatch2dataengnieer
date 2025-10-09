Write  a  program  to  convert  infix  to  prefix
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0
def isOperator(c):
    return c in "+-*/^"
def infixToPrefix(expression):
    expression = expression[::-1]
    expression = list(expression)
    for i in range(len(expression)):
        if expression[i] == '(':
            expression[i] = ')'
        elif expression[i] == ')':
            expression[i] = '('
    expression = ''.join(expression)
    stack = []      
    result = []     
    for ch in expression:
        if ch.isalnum():
            result.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(ch) < precedence(stack[-1]):
                result.append(stack.pop())
            stack.append(ch)
    while stack:
        result.append(stack.pop())
    prefix = ''.join(result[::-1])
    return prefix
expr = input("Enter infix expression: ")
print("Prefix expression:", infixToPrefix(expr))

Write  a  program  to  evaluate  prefix  expression
def evaluatePrefix(expression):
    stack = []
    for ch in expression[::-1]:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            a = stack.pop()
            b = stack.pop()
            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)
    return stack[0]
expr = input("Enter prefix expression: ")
print("Result =", evaluatePrefix(expr))
