#postfix to prefix 
from stack import stack
def convert(postfix):
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
postfix=input("Enter Postfix Expression : ")
print("Prefix Expression is : ",convert(postfix))