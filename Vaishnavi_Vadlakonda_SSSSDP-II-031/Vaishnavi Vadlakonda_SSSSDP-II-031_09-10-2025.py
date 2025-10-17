'''
Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix to prefix
'''
from prog1b import stack
def icp(operator):
    if operator in '+-':
        return 2
    if operator in '*/%':
        return 3
    if operator == '^':
        return 4
    if operator == ')':
        return 5
def isp(operator):
    match operator:
        case '+'|'-':
            return 1
        case '*'|'/'|'%':
            return 2
        case '^':
            return 4
        case ')':
            return 0
        case '#':
            return -1
def convert(infix):
    infix = infix[::-1]
    s = stack()
    s.push('#')
    prefix = ''
    for ch in infix:
        if ch.isdigit():
            prefix += ch
        elif ch == '(':
            while s.peek() != ')':
                prefix += s.pop()
            s.pop()
        else:
            while icp(ch) <= isp(s.peek()):
                prefix += s.pop()
            s.push(ch)   
    while s.peek() != '#':
        prefix += s.pop()
    return prefix[::-1]
if __name__ == '__main__':
    infix = input("Enter infix expression:")
    prefix = convert(infix) 
    print('Prefix expression:', prefix)
'''
Outputs
Enter infix expression:3+4
Prefix expression: +34
'''








'''
Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4 * 3 + -
'''
from prog9b import *
def eval(prefix):
    prefix = prefix[::-1]
    s = stack()
    for ch in prefix:
        if ch.isdigit():
            s.push(int(ch))
        else:
            x = s.pop()
            y = s.pop()
            match ch:
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
infix = input("Enter prefix expression:")
prefix = convert(infix)
print('Result:', eval(prefix))
'''
Outputs
Enter prefix expression:3+4*6/2
Result: 15.0
'''