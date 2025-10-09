'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from stack import stack
def  icp(operator):
    if operator=='+' or operator=='-':
        return 1 #return  1  when  operator  is   +  (or)  -
    elif operator=='*' or operator=='/' or operator=='%':
        return 2 #return  2  when  operator  is   * , /   (or)  %
    elif operator=='(' or operator=='^':
        return 4
     #return  4  when  operator  is   (  (or)  ^
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
    if operator=='+' or operator=='-':
        return 1 #return  1  when  operator  is   +  (or)  -
    elif operator=='*' or operator=='/' or operator=='%':
        return 2 #return  2  when  operator  is   * , /   (or)  %
    elif operator=='^':
        return 3
    elif operator=='(':
        return 0
    elif operator=='#':
        return -1
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  ---> -1
'''
def  convert(infix):
    s=stack()
    s.push('#')
    s.postfix='' 
    for char in infix:
        if  char.isalnum():
            s.postfix+=char
        elif  char  ==  ')':
            while not s.peek()=='(':
                x=s.pop()
                s.postfix+=x
            if s.peek()=='(':
                s.pop()
        else:
            if icp(char) > isp(s.peek()):
                s.push(char)
            else:
                while icp(char)<=isp(s.peek()):
                    x=s.pop()
                    s.postfix+=x
                if icp(char)>isp(s.peek()):
                    s.push(char)
    while not s.peek()=='#':
        x=s.pop()
        s.postfix+=x
    return s.postfix
#  End  of  the  function
if __name__=='__main__':
    infix=input("Enter infix Expression")#How  to  read  infix  expression
    postfix=convert(infix) #How  to  convert  infix  expression  to  postfix expression
    print('Postfix Expression :',postfix)