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
if __name__=='__main__':
    infix=input("Enter infix expression : ")
    infix=infix[::-1]
    prefix=convert(infix)
    print('Prefix Expression : ',prefix[::-1])
            
            
