                         NAME:M.SAICHARAN                     HOMEWORK
                         DATE:09-10-2025

'''
1.Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
#Program:
def icp(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/', '%'):
        return 2
    elif operator in ('(', '^'):
        return 4
    return 0
def isp(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/', '%'):
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 0
    elif operator == '#':
        return -1
    return 0
def reverse_expression(expr):
    expr = expr[::-1]
    new_expr = ""
    for ch in expr:
        if ch == '(':
            new_expr += ')'
        elif ch == ')':
            new_expr += '('
        else:
            new_expr += ch
    return new_expr
def infix_to_postfix(infix):
    stack = []
    stack.append('#')
    postfix = ''

    for ch in infix:
        if ch.isalnum():          
            postfix += ch
        elif ch == ')':           
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()          
        else:                     
            while icp(ch) <= isp(stack[-1]):
                postfix += stack.pop()
            stack.append(ch)

    while stack[-1] != '#':
        postfix += stack.pop()

    return postfix

def infix_to_prefix(infix):
    reversed_infix = reverse_expression(infix)  
    postfix_expr = infix_to_postfix(reversed_infix) 
    prefix_expr = postfix_expr[::-1]
    return prefix_expr

infix = input("Enter infix expression: ")
prefix = infix_to_prefix(infix)
print("Prefix expression:", prefix)


'''
2.Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''
#Program:
def eval_prefix(expression):
    stack = []
    tokens = expression.split()[::-1]
    for ch in tokens:
        if ch.isdigit():    
            stack.append(int(ch))
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
            elif ch == '^':
                stack.append(a ** b)
    return stack.pop()
prefix = input("Enter prefix expression: ")
result = eval_prefix(prefix)
print("Result of prefix expression:", result)
