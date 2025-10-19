# -------------------------------- PREFIX TO POSTFIX CONVERSION -----------------------------

#Prefix to postfix
from infixtoprefix import *
def prefix_to_postfix(prefix):
    prefix=prefix[::-1]
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
infix=input("Enter infix expression : ")
prefix=convert(infix)
print("Postfix Expression is : ",prefix_to_postfix(prefix))