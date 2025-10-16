'''
Write  a  program  to  convert  infix  to  prefix
Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
from progb import *
def infix_to_prefix(infix):
    stack = []
    prefix = []
    infix = infix[::-1]
    for char in infix:
        if char.isalnum():
            prefix.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            stack.pop()
        else:
            while (stack and precedence(stack[-1]) > precedence(char)):
                prefix.append(stack.pop())
            stack.append(char)
    while stack:
        prefix.append(stack.pop())
    return ''.join(prefix[::-1])
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0
infix = input("Enter infix expression: ")
prefix = infix_to_prefix(infix)
print("Prefix expression:", prefix)

'''
Write  a  program  to  evaluate  prefix  expression
Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''
def evaluate_prefix(prefix):
    stack = []
    prefix = prefix.split()[::-1]
    for char in prefix:
        if char.isdigit():
            stack.append(int(char))
        else:
            a = stack.pop()
            b = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
    return stack[0]
prefix = input("Enter prefix expression (space separated): ")
result = evaluate_prefix(prefix)
print("Result of prefix evaluation:", result)   
