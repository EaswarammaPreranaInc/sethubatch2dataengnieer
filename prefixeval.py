'''
Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4 * 3 + -
'''

from infixtoprefix import *
def eval(prefix):
    s=stack()
    for ch in prefix:
        if ch.isdigit():
            s.push(int(ch))
        else:
            x=s.pop()
            y=s.pop()
            match ch:
                case '+':
                    s.push(x+y)
                case '-':
                    s.push(x-y)
                case '*':
                    s.push(x*y)
                case '/':
                    s.push(x//y)
                case '^':
                    s.push(x**y)
    return s.pop()
infix=input("Enter infix expression : ")
prefix=convert(infix[::-1])
print('Result : ',eval(prefix))



