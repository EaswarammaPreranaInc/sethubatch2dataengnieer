from infix_to_postfix import *
def eval(postfix):
    s=stack()
    for ch in postfix:
        # print(ch)
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
infix=input("Enter infix: ")
postfix=convert(infix)
print(postfix)
print(eval(postfix))