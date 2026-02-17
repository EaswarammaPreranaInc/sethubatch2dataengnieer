''' 1) Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix  to  prefix
'''

from prog1b import stack
def icp(operator):
    if operator in '+-':
        return 2  # icp  of  '+'  and  '-'  is   1
    if operator in '*/%':
        return 3  # icp  of  '*' ,  '/'   and  '%'  is   2
    if operator in '^':
        return 4  # icp  of  '('  and  '^'  is    4
    if operator in ')':
        return 5

def isp(operator):
    match operator:
        case '+' | '-':
            return 1  # isp  of  '+'  and  '-'  is   1
        case '*' | '/' | '%':
            return 2  # isp  of  '*' ,  '/'   and  '%'  is   2
        case '^':
            return 4  # isp  of   '^'   is   3
        case '(':
            return 0  # isp  of   '('   is   0
        case '#':
            return -1  # isp  of   '#'   is   -1

def convert(infix):
    infix=infix[::-1]
    s = stack()     # Constructor  initializes  object  with  list  =  []
    s.push('#')     # Pushes  '#'  into  the  stack
    prefix = ''    # Empty  string
    for ch in infix:        # ch  is  each  char   of  infix  expression
        if ch.isalnum():    # Is  ch  an  operand
            prefix += ch   # Concatenates  the  operand  to  prefix  expression
        elif ch == '(':
            while s.peek() != ')':  # Repeat  until  ''  is  last  element  of  the  stack
                prefix += s.pop()  # Removes  each  operator  of  the  stack  and  concatenates  the  deleted  operator  to  prefix  expression
            s.pop()                 # Removes  '('  from  stack  and  is  ignored  (not  concatenated  to  prefix  expression)
        else:
            while icp(ch) <= isp(s.peek()):  # Repeat  until  icp  of  the  operator  >  isp  of  last  element  of  the  stack
                prefix += s.pop()  # Removes  each  operator  of  the  stack  and  concatenates  the  deleted  operator  to  prefix  expression
            s.push(ch)              # Pushes  the  operator  into  the  stack  as  soon  as   icp  >  isp
    # End  of  for  loop
    while s.peek() != '#':  # Repeat  until  '#'  is  last  element  of  the  stack
        prefix += s.pop()  # Removes  each  operator  of  the  stack  and  concatenates  the  deleted  operator  to  prefix  expression
    return prefix[::-1]
# End  of  the  function

if __name__ == '__main__':
    infix = input('Enter  infix  expression  :  ')  # Reads  infix  expression
    prefix = convert(infix)  # Converts  infix  expression  to  prefix  expression
    print('prefix  expression :  ', prefix)


''' 2) Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''
from progr9b import *
def eval(prefix):
    s=stack()
    prefix = prefix[::-1]
    for ch in prefix:
        if ch.isdigit():
            s.push(int(ch))
        else:
            a = s.pop()
            b = s.pop()
            if ch == '+':
                s.push(a + b)
            elif ch == '-':
                s.push(a - b)
            elif ch == '*':
                s.push(a * b)
            elif ch == '/':
                s.push(a // b)
            elif ch ==  '^':
                s.push(a**y)    
    return s.pop()
infix = input("Enter prefix expression: ")
prefix=convert(infix)
print("Result of prefix evaluation:", prefix)   
