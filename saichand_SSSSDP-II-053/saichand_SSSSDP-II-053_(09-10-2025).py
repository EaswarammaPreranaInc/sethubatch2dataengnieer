'''
Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
#Program:
from prog1b import stack
def icp(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/' or operator == '%':
        return 2
    if operator == '^':
        return 4
    if operator == ')':
        return 4
def isp(operator):
    match operator:
        case '+' | '-':
            return 1
        case '*' | '/' | '%':
            return 2
        case '^':
            return 3
        case ')':
            return 0
        case '#':
            return -1
def reverse_and_swap(expression):
    expression = expression[::-1]
    expression = expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    return expression
def convert_infix_to_postfix(infix):
    s = stack()
    s.push('#')
    postfix = ""
    for char in infix:
        if char.isdigit():
            postfix += char
        elif char == '(':
            s.push(char)
        elif char == ')':
            while s.peek() != '(':
                postfix += s.pop()
            s.pop()
        else:
            while icp(char) <= isp(s.peek()):
                postfix += s.pop()
            s.push(char)
    while s.peek() != '#':
        postfix += s.pop()
    return postfix
def infix_to_prefix(infix):
    infix = reverse_and_swap(infix)
    postfix = convert_infix_to_postfix(infix)
    prefix = postfix[::-1]
    return prefix
infix = input("Enter infix expression: ")
prefix = infix_to_prefix(infix)
print("Prefix Expression:", prefix)






'''
Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''
#Program:
from prog1b import stack
def eval_prefix(prefix):
    s = stack()
    prefix = prefix.split()
    for char in reversed(prefix):
        if char.isdigit():
            s.push(int(char))
        else:
            y = s.pop()
            x = s.pop()
            match char:
                case '+':
                    s.push(x + y)
                case '-':
                    s.push(x - y)
                case '*':
                    s.push(x * y)
                case '/':
                    s.push(x / y)
                case '^':
                    s.push(x ** y)
    return s.pop()
prefix = input("Enter prefix expression: ")
result = eval(prefix)
print("Result of prefix expression:", result)