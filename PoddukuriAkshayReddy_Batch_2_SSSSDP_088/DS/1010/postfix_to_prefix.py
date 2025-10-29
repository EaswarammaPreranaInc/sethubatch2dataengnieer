# 
# from numpy import stack

from DS.0810.infix_to_postfix import stack


def postfix_prefix(postfix):
    s = stack()
    for char in postfix:
        if char.isalnum():
            s.push(char)
        else:
            op1 = s.pop()
            op2 =  s.pop()
            new_expr = char + op2 + op1
            s.push(new_expr)
    return s.pop()


postfix = input("Enter Postfix Expression: ")
print("Prefix Expression:", postfix_prefix(postfix))