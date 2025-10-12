''' 1) Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''

from prog1b import stack

def icp(operator):
    if operator in '+-':
        return 1  # icp  of  '+'  and  '-'  is   1
    if operator in '*/%':
        return 2  # icp  of  '*' ,  '/'   and  '%'  is   2
    if operator in '(^':
        return 4  # icp  of  '('  and  '^'  is    4

def isp(operator):
    match operator:
        case '+' | '-':
            return 1  # isp  of  '+'  and  '-'  is   1
        case '*' | '/' | '%':
            return 2  # isp  of  '*' ,  '/'   and  '%'  is   2
        case '^':
            return 3  # isp  of   '^'   is   3
        case '(':
            return 0  # isp  of   '('   is   0
        case '#':
            return -1  # isp  of   '#'   is   -1

def convert(infix):
    s = stack()     # Constructor  initializes  object  with  list  =  []
    s.push('#')     # Pushes  '#'  into  the  stack
    postfix = ''    # Empty  string
    for ch in infix:        # ch  is  each  char   of  infix  expression
        if ch.isalnum():    # Is  ch  an  operand
            postfix += ch   # Concatenates  the  operand  to  postfix  expression
        elif ch == ')':
            while s.peek() != '(':  # Repeat  until  '('  is  last  element  of  the  stack
                postfix += s.pop()  # Removes  each  operator  of  the  stack  and  concatenates  the  deleted  operator  to  postfix  expression
            s.pop()                 # Removes  '('  from  stack  and  is  ignored  (not  concatenated  to  postfix  expression)
        else:
            while icp(ch) <= isp(s.peek()):  # Repeat  until  icp  of  the  operator  >  isp  of  last  element  of  the  stack
                postfix += s.pop()  # Removes  each  operator  of  the  stack  and  concatenates  the  deleted  operator  to  postfix  expression
            s.push(ch)              # Pushes  the  operator  into  the  stack  as  soon  as   icp  >  isp
    # End  of  for  loop
    while s.peek() != '#':  # Repeat  until  '#'  is  last  element  of  the  stack
        postfix += s.pop()  # Removes  each  operator  of  the  stack  and  concatenates  the  deleted  operator  to  postfix  expression
    return postfix
# End  of  the  function
if __name__ == '__main__':
    infix = input('Enter  infix  expression  :  ')  # Reads  infix  expression
    postfix = convert(infix)  # Converts  infix  expression  to  postfix  expression
    print('Postfix  expression :  ', postfix)






''' 
2) Write  a  program  to  evaluate  postfix  expression

Input :  3 4 5 * + 6 2 / -
Output :  20

'''

from prog7b import *  #  Imports   stack  class , icp() , isp() , convert() functions  and   the  if  statement  outside  the  functions
def eval(postfix):
    s = stack()  #   Constructor  initializes  object  with  list  =  []
    for ch in postfix:  #  ch  is  each  char   of  postfix  expression
        if ch.isdigit():  #  Is  the  char  an  operand
            s.push(int(ch))  #  Convert  the  char  to  integer  and  push  to  the  stack
        else:  #   ch  is  an  operator
            y = s.pop()  #  First  deleted  element  is  the   2nd  operand
            x = s.pop()  #  2nd  deleted  element  is  the   1st  operand
            match ch:  #  What  is  the  operator ?
                case '+':
                    s.push(x + y)  #  push  the  result  of  x + y  into  the  stack
                case '-':
                    s.push(x - y)  #  push  the  result  of  x - y  into  the  stack
                case '*':
                    s.push(x * y)  #  push  the  result  of  x * y  into  the  stack
                case '/':
                    s.push(x // y)  #  push  the  result  of  x // y  into  the  stack
                case '^':
                    s.push(x ** y)  #  push  the  result  of  x ** y  into  the  stack
    #  End  of  for  loop
    return s.pop()  #  The  result  of  postfix  expression
#  End  of  the  function
infix = input('Enter  infix  expression  :  ')  #   Reads  infix  expression
postfix = convert(infix)    #  Converts  infix  to  postfix
print('Result : ', eval(postfix))   



