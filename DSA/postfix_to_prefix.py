# ------------------------ POSTFIX TO PREFIX CONVERSION -----------------------------

#postfix to prefix 
from infixtopostfix import *
def postfix_to_prefix(postfix):
    s=stack()
    prefix=''
    for ch in postfix:
        if ch.isalnum():
            s.push(ch)
        else:
            y=s.pop()
            x=s.pop()
            prefix=ch+x+y
            s.push(prefix)
    return s.pop()
infix=input("Enter infix Expression : ")
postfix=convert(infix)
print("Prefix Expression is : ",postfix_to_prefix(postfix))