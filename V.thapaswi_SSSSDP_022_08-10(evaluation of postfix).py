
'''
Write  a  program  to  evaluate  postfix  expression
Posifix  expression  --->    3 4 5 * + 6 2 / -
'''
from infix_to_postfix import *
def eval(postfix):
    s=stack()
    for x in postfix:
        if x.isdigit():
            s.push(int(x))
        else:
            b=s.pop()
            a=s.pop()
            match x:
                case '+':
                    s.push(a+b)
                case '-':
                    s.push(a-b)
                case '*':
                    s.push(a*b)
                case '/':
                    s.push(a//b)
                case '^':
                    s.push(a**b)
    return s.pop()
infix=input("Enter infix expression :")
postfix=convert(infix)
print('postfix :',postfix)
print('Result: ',eval(postfix))
        
'''
o/p:
Enter infix expression :3+4*5-6/2
postfix :  345*+62/-
Result:  20
'''