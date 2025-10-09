from infix_to_prefix import *
def eval(prefix):
    s=stack()
    prefix_rev=prefix[::-1]
    for ch in prefix_rev:
        if ch.isdigit():
            s.push(int(ch))
        else:
            y=s.pop()
            x=s.pop()
            match ch:
                case '+':s.push(x+y)
                case '-':s.push(x-y)
                case '*':s.push(x*y)
                case '^':s.push(x**y)
                case '/':s.push(x//y)
                case '%':s.push(x%y)
    return s.peek()
infix=input("Enter infix:")
prefix=convert(infix)
print(eval(prefix))