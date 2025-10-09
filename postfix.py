'''
Write  a  program  to  evaluate  postfix  expression

Posifix  expression  --->    3 4 5 * + 6 2 / -
'''
from infixtopostfix import convert
from stack import stack
def  eval(a):
    s=stack()
    for char in a:
        if  char.isalnum():
            s.push(int(char))
        else:
            y=s.pop()
            x=s.pop()
            match char:
                case   '+':  s.push(x+y)
                case   '-':  s.push(x-y)
                case   '*':  s.push(x*y)
                case   '/':  s.push(x//y)
                case   '^':  s.push(x**y)
    return  s.peek()
#  End  of  the  function
infix=input("Enter infix Expression : ")#How  to  read  infix  expression
postfix=convert(infix) #How  to  convert infix  to  postfix
result=eval(postfix)#How  to  evaluate  postfix  expression
print('Result : ',result)