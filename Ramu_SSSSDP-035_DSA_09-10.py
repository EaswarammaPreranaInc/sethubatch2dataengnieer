#Ramu(09-10)

'''
Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix to prefix
'''

from stack import stack
def icp(op):
    if op in '+-':
        return 2
    if op in '*/%':
        return 3
    if op in '^':
        return 4
    if op in ')':
        return 5
def isp(op):
    if op in '+-':
        return 1
    if op in '*/%':
        return 2
    if op in '^':
        return 4
    if op in ')':
        return 0
    if op in '#':
        return -1
def convert(infix):
    s=stack()
    s.push('#')
    prefix=''
    for ch in infix:
        if ch.isalnum():
            prefix+=ch
        elif ch=='(':
            while s.peek()!=')':
                prefix+=s.pop()
            s.pop()
        else:
            if icp(ch)>isp(s.peek()):
                s.push(ch)
            else:
                while(icp(ch)<=isp(s.peek())):
                    prefix+=s.pop()
                s.push(ch)
    while s.peek()!='#':
        prefix+=s.pop()
    return prefix
if _name=='main_':
    infix=input("Enter infix expression : ")
    infix=infix[::-1]
    prefix=convert(infix)
    print('Prefix Expression : ',prefix[::-1])
            
            
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