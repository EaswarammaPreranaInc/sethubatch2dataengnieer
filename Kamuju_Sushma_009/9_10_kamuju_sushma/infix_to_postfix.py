from stack import stack 
def icp(ch):
    if ch in '+-':
        return 1
    elif ch in '*/%':
        return 2
    elif ch =='^' or ch=='(':
        return 4
def isp(ch):
    if ch in '+-':
        return 1
    elif ch in '*/%':
        return 2 
    elif ch =='^':
        return 3
    elif ch =='(':
        return 0
    elif ch=='#':
        return -1
def convert(infix):
    postfix=""
    s=stack()
    s.push('#')
    # print(infix)
    for ch in infix:
        # print(ch)
        if ch.isalnum():
            postfix+=ch
        elif ch==')':
            while s.peek()!='(':
                postfix+=s.pop()
            s.pop()
        elif icp(ch)>isp(s.peek()):
            s.push(ch)
        else:
            while(icp(ch)<=isp(s.peek())):
                postfix+=s.pop()
            s.push(ch)
    while(s.peek()!='#'):
        postfix+=s.pop()
    return postfix
if __name__=='__main__':
    infix=input("Enter prefix:")
    postfix=convert(infix)
    print(postfix)
        # else:
        #     if icp(ch)>isp(s.peek()):
        #         s.push(ch)
        #     elif 