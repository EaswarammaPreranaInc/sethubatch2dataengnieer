def infix_to_postfix(expression):
    # Precedence levels (higher number = higher precedence)
    
    priority = { '+': 1, '-': 1, '*': 2, '/': 2, '^': 3 }
    op_stack = []
    output = []

    for symbol in expression.split():
        if symbol.isalnum():     # Operand (number or variable)
            output.append(symbol)

        elif symbol == '(':
            op_stack.append(symbol)

        elif symbol == ')':
            while op_stack and op_stack[-1] != '(':
                output.append(op_stack.pop())
            if op_stack:
                op_stack.pop()   # remove '('

        else:   # Operator
            # Handle right-associativity for ^
            while ( op_stack 
                    and op_stack[-1] != '(' 
                    and ( priority.get(op_stack[-1], 0) > priority.get(symbol, 0) 
                          or ( priority.get(op_stack[-1], 0) == priority.get(symbol, 0) 
                               and symbol != '^' ) ) ):
                output.append(op_stack.pop())
            op_stack.append(symbol)

    while op_stack:
        output.append(op_stack.pop())

    return " ".join(output)


# Example
infix_expr = input("Enter infix expression (space separated): ")
print("Postfix:", infix_to_postfix(infix_expr))
