'''
Write  a  program  to  evaluate  prefix  expression
Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''

from infix_to_prefix import *

def eval(infix):
    st=stack()
    for ch in infix:
        if ch.isdigit():
            st.push(int(ch))
        else:
            x=st.pop()
            y=st.pop()
            
            match ch:
                case '+':
                    st.push(x+y)
                case '-':
                    st.push(x-y)
                case '*':
                    st.push(x*y)
                case '/':
                    st.push(x//y)
                case '^':
                    st.push(x**y)
    return st.peek()
    
        
infix=input("Enter Infix Expression :")
infix=infix[::-1]
prefix=convert(infix)
prefix=prefix[::-1]
result=eval(prefix)
print(result)


