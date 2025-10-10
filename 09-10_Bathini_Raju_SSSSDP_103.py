'''
Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix  to  prefix
'''

from stack import stack

def icp(operator):
    if operator == '+' or operator == '-':
        return 2
    if operator == '*' or operator == '/' or operator == '%':
        return 3
    if operator == ')':
        return 5
    if operator=='^':
        return 4
    return 0


def isp(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/' or operator == '%':
        return 2
    if operator == '^':
        return 4
    if operator == ')':
        return 0
    if operator == '#':
        return -1
    return 0

def convert(infix):
    st=stack()
    st.push('#')
    prefix=''
    for ch in infix:
        if ch.isalnum():
            prefix+=ch
        elif ch=='(':
            while st.peek() != ')':
                prefix+=st.pop()
            st.pop()
        else:
            if icp(ch)>isp(st.peek()):
                st.push(ch)
            else:
                while icp(ch)<=isp(st.peek()):
                    prefix+=st.pop()
                st.push(ch)
    while st.peek() !='#':
        prefix+=st.pop()
    return prefix[::-1]

                        
    
    
if __name__=='__main__':
    infix=input("Enter infix Expression :")
    infix=infix[::-1]
    prefix=convert(infix)
    print(prefix)
