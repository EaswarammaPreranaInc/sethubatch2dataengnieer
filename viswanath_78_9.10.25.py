			DSA programming

q) Write  a  program  to  convert  infix  to  prefix
Hint:  Modify  following  program  to  convert  infix  to  prefix
Ans)   from prog1b import stack
def icp(operator):
    if operator in '+-':
        return 1
    elif operator in '*/%':
        return 2
    elif operator == '^' or operator == '(':
        return 4
def isp(operator):
    if operator in '+-':
        return 1
    elif operator in '*/%':
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 0
    elif operator == '#':
        return -1
def infix_to_postfix(infix):
    s = stack()
    s.push('#')
    postfix = ''
    for ch in infix:
        if ch.isalnum():
            postfix += ch
        elif ch == ')':
            while s.list[-1] != '(':
                postfix += s.pop()
            s.pop()  # Remove '('
        else:  # Operator
            while icp(ch) <= isp(s.list[-1]):
                postfix += s.pop()
            s.push(ch)
    while s.list[-1] != '#':
        postfix += s.pop()
    return postfix
def infix_to_prefix(infix):
    infix = infix[::-1]
    infix = ''.join(['(' if ch == ')' else ')' if ch == '(' else ch for ch in infix])
    postfix = infix_to_postfix(infix)
    prefix = postfix[::-1]
    return prefix
infix_expr = input("Enter infix expression: ")
prefix_expr = infix_to_prefix(infix_expr)
print("Prefix expression:", prefix_expr)


q) Write  a  program  to  evaluate  prefix  expression
Prefix  expression :   -  +  3  *  4  5  /  6  2
Ans) class stack:
    def __init__(self):
        self.list = []
    def push(self, x):
        self.list.append(x)
    def pop(self):
        return self.list.pop()
def evaluate_prefix(expr):
    s = stack()
    tokens = expr.split()[::-1]      # Reverse the prefix expression
    for ch in tokens:
        if ch.isdigit():             # Operand → push to stack
            s.push(int(ch))
        else:                        # Operator → pop 2 operands
            op1 = s.pop()
            op2 = s.pop()
            if ch == '+':
                s.push(op1 + op2)
            elif ch == '-':
                s.push(op1 - op2)
            elif ch == '*':
                s.push(op1 * op2)
            elif ch == '/':
                s.push(op1 / op2)
            elif ch == '%':
                s.push(op1 % op2)
            elif ch == '^':
                s.push(op1 ** op2)
    return s.pop()
expr = "- + 3 * 4 5 / 6 2"
result = evaluate_prefix(expr)
print("Result:", result)  
