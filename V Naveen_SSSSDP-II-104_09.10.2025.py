'''
Write  a  program  to  convert  infix  to  prefix
Hint:  Modify  following  program  to  convert  infix to prefix
'''

# Function to check operator precedence
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return 0

# Function to check if character is operator
def isOperator(c):
    return c in ['+', '-', '*', '/', '^']

# Function to convert infix to prefix
def infix_to_prefix(expr):
    # Step 1: Reverse the infix expression
    expr = expr[::-1]

    # Step 2: Swap '(' with ')' and vice versa
    expr = list(expr)
    for i in range(len(expr)):
        if expr[i] == '(':
            expr[i] = ')'
        elif expr[i] == ')':
            expr[i] = '('
    expr = "".join(expr)

    stack = []   # operator stack
    result = []  # output list

    # Step 3: Convert reversed infix to postfix (normal algorithm)
    for ch in expr:
        if ch.isalnum():        # operand
            result.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # remove '('
        else:  # operator
            while stack and precedence(stack[-1]) >= precedence(ch):
                result.append(stack.pop())
            stack.append(ch)

    # Step 4: Pop remaining operators
    while stack:
        result.append(stack.pop())

    # Step 5: Reverse the result to get prefix
    prefix = "".join(result[::-1])
    return prefix

expr = input("Enter infix expression: ")
print("Prefix expression:", infix_to_prefix(expr))


'''
Write  a  program  to  evaluate  prefix  expression
Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4 * 3 + -
'''

def eval_prefix(expr):
    stack = []
    operators = ['+', '-', '*', '/', '^']

    # Step 1: Reverse the prefix expression (split by space)
    tokens = expr.split()[::-1]

    # Step 2: Scan from left to right (since reversed)
    for token in tokens:
        if token not in operators:
            # Operand → push to stack
            stack.append(float(token))
        else:
            # Operator → pop two operands
            op1 = stack.pop()
            op2 = stack.pop()

            # Perform operation
            if token == '+':
                result = op1 + op2
            elif token == '-':
                result = op1 - op2
            elif token == '*':
                result = op1 * op2
            elif token == '/':
                result = op1 / op2
            elif token == '^':
                result = op1 ** op2

            # Push result back to stack
            stack.append(result)

    # Step 3: Final result
    return stack[0]

expr = input("Enter prefix expression: ")
print("Reverse of prefix:", " ".join(expr.split()[::-1]))
print("Result:", eval_prefix(expr))
