
'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from stack import stack

def icp(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/' or operator == '%':
        return 2
    if operator == '(' or operator == '^':
        return 4
    return 0
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''

def isp(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/' or operator == '%':
        return 2
    if operator == '^':
        return 3
    if operator == '(':
        return 0
    if operator == '#':
        return -1
    return 0
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  ---> -1
'''

def convert(infix):
    st = stack()
    st.push('#')  # How  to  push  '#'  into  the  stack 
    st.postfix = ''

    for char in infix:
        if char.isalnum():   # How  to  check  whether  char  is  operand
            st.postfix += char

        elif char == ')':
            while st.peek() != '(':
                st.postfix += st.pop()
            st.pop()   # remove '('

        elif char == '(':
            st.push(char)

        else:  # operator case
            while icp(char) <= isp(st.peek()):
                st.postfix += st.pop()
            st.push(char)

    #  End  of  for  loop
    while st.peek() != '#':
        st.postfix += st.pop()

    return st.postfix

#  End  of  the  function


'''
Write  a  program  to  evaluate  postfix  expression

Posifix  expression  --->    3 4 5 * + 6 2 / -
'''

def  eval(a):
    st=stack()
    for char in a:
        if  char.isalnum():
            st.push(int(char))
        else:
            y=st.pop()
            x=st.pop()
            
            match char :
                case '+': st.push(x+y)
                case '-':  st.push(x-y)
                case   '*': st.push(x*y)
                case   '/': st.push(x/y)
                case   '^': st.push(x**y)
    return  st.peek()
#  End  of  the  function
infix=input("Enter infix Expression :")
p=convert(infix) #How  to  convert infix  to  postfix
print("postfix Expression :" ,p)
res=eval(p)
print("Postfix Evaluation :",res)