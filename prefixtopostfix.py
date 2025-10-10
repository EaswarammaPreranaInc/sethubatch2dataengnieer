#Prefix to postfix
from stack import stack
def convert(prefix):
    s=stack()
    postfix=''
    for ch in prefix:
        if ch.isalnum():
            s.push(ch)
        else:
            x=s.pop()
            y=s.pop()
            postfix=x+y+ch
            s.push(postfix)
    return s.pop()
prefix=input("Enter prefix expression : ")
print("Postfix Expression is : ",convert(prefix[::-1]))