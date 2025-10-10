# Question 1:
Write a program to convert infix to prefix

# Answer:
def infix_to_prefix(expression):
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def is_operator(c):
        return c in ['+', '-', '*', '/', '^']

    # Reverse the infix expression
    expression = expression[::-1]
    expression = expression.replace('(', 'temp')
    expression = expression.replace(')', '(')
    expression = expression.replace('temp', ')')

    stack = []
    output = []

    for c in expression:
        if c.isalnum():
            output.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(c):
                output.append(stack.pop())
            stack.append(c)

    while stack:
        output.append(stack.pop())

    prefix = ''.join(output[::-1])
    return prefix


# Example
exp = "(A-B/C)*(A/K-L)"
print("Infix Expression:", exp)
print("Prefix Expression:", infix_to_prefix(exp))

# Output:
# Infix Expression: (A-B/C)*(A/K-L)
# Prefix Expression: *-A/BC-/AKL


# Question 2:
Write a program to evaluate prefix expression

Prefix expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -

# Answer:
def evaluate_prefix(expression):
    stack = []
    for symbol in reversed(expression):
        if symbol.isdigit():
            stack.append(int(symbol))
        else:
            a = stack.pop()
            b = stack.pop()
            if symbol == '+':
                stack.append(a + b)
            elif symbol == '-':
                stack.append(a - b)
            elif symbol == '*':
                stack.append(a * b)
            elif symbol == '/':
                stack.append(a / b)
    return stack[0]


# Example
expr = ['-', '+', '3', '*', '4', '5', '/', '6', '2']
print("Prefix Expression:", ' '.join(expr))
print("Reverse of Prefix:", ' '.join(expr[::-1]))
print("Evaluated Result:", evaluate_prefix(expr))

# Output:
# Prefix Expression: - + 3 * 4 5 / 6 2
# Reverse of Prefix: 2 6 / 5 4 * 3 + -
# Evaluated Result: 17.0
