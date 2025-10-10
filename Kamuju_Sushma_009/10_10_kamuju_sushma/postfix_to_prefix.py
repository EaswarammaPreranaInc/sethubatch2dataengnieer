#  Write  a  program  to  convert  postfix  to  prefix
# from stack import stack
from infix_to_postfix import *
def convert_postfix_to_prefix(postfix):
    s=stack()
    for ch in postfix:
        if ch.isalnum():
            s.push(ch)
        else:
            y=s.pop()
            x=s.pop()
            s.push(ch+x+y)
    return s.pop()

infix=input("Enter infix:")
postfix=convert(infix)
print(convert_postfix_to_prefix(postfix))
