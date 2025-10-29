



def prefix_postfix(prefix):
    s = stack()
    for char in prefix[::-1]:
        if char.isalnum():
            s.push(char)
        else:
            op1 = s.pop()
            op2 = s.pop()
            new_expr = op1 + op2 + char
            s.push(new_expr)
    return s.pop()