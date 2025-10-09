'''
Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
from stack import stack
def icp(ch):
    if ch in '+-':
        return 2
    elif ch in '*/%':
        return 3
    elif ch=='^':
        return 4
    elif ch==')':
        return 5
def isp(ch):
    match ch:
        case '+'|'-': return 1
        case '*'|'/'|'%': return 2
        case '^':return 4
        case ')':return 0
        case '#':return -1
def convert(infix):
    prefix=""
    s=stack()
    s.push('#')
    infix=infix[::-1]
    for ch in infix:
        if ch.isalnum():
            prefix+=ch
        elif ch=='(':
            while s.peek()!=')':
                prefix+=s.pop()
            s.pop()
        elif icp(ch)>isp(s.peek()):
            s.push(ch)
        else:
            while icp(ch)<=isp(s.peek()):
                prefix+=s.pop()
            s.push(ch)
    while s.peek()!='#':
        prefix+=s.pop()
    return prefix[::-1]
if __name__=='__main__':
    infix=input("Enter infix:")
    prefix=convert(infix)
    print(prefix)