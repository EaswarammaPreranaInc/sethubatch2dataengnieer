from infix_to_prefix import *
def convert_prefix_to_postfix(prefix):
    prefix=prefix[::-1]
    s=stack()
    for ch in prefix:
        if ch.isalnum():
            s.push(ch)
        else:
            x=s.pop()
            y=s.pop()
            s.push(x+y+ch)
    return s.pop()
infix=input("Enter infix:")
prefix=convert_infix_to_prefix(infix)
postfix=convert_prefix_to_postfix(prefix)

