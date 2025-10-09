'''
Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix to prefix
'''


class InfixToPrefix:
    def __init__(self, expr):
        self.expr = expr
        self.stack = []
        self.result = ""

    def precedence(self, ch):
        if ch in ('+', '-'):
            return 1
        elif ch in ('*', '/'):
            return 2
        elif ch == '^':
            return 3
        else:
            return 0

    def infix_to_postfix(self, expr):
        for ch in expr:
            if ch.isalnum():     # operand (A-Z, a-z, 0-9)
                self.result += ch
            elif ch == '(':
                self.stack.append(ch)
            elif ch == ')':
                while self.stack and self.stack[-1] != '(':
                    self.result += self.stack.pop()
                self.stack.pop()  # remove '('
            else:  # operator
                while (self.stack and 
                       self.precedence(ch) <= self.precedence(self.stack[-1])):
                    self.result += self.stack.pop()
                self.stack.append(ch)

        # pop remaining operators
        while self.stack:
            self.result += self.stack.pop()
        return self.result

    def infix_to_prefix(self):
        # Step 1: Reverse the infix
        rev = ""
        for ch in self.expr[::-1]:
            if ch == '(':
                rev += ')'
            elif ch == ')':
                rev += '('
            else:
                rev += ch
        # Step 2: Convert reversed infix to postfix
        postfix = self.infix_to_postfix(rev)

        # Step 3: Reverse postfix → prefix
        prefix = postfix[::-1]
        return prefix
# Example:
expression = input("Enter infix expression: ")
converter = InfixToPrefix(expression)
prefix = converter.infix_to_prefix()
print("Prefix Expression:", prefix)


'''
Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''

class PrefixEvaluation:
    def __init__(self, expr):
        self.expr = expr.split()  
        self.stack = []
    def evaluate(self):
        rev_expr = self.expr[::-1]
        for ch in rev_expr:
            if ch.isdigit():   # Operand (0-9)
                self.stack.append(int(ch))
            else:  # Operator
                x = self.stack.pop()
                y = self.stack.pop()

                if ch == '+':
                    self.stack.append(x + y)
                elif ch == '-':
                    self.stack.append(x - y)
                elif ch == '*':
                    self.stack.append(x * y)
                elif ch == '/':
                    self.stack.append(x / y)
        return self.stack.pop()

expr = input("Enter Prefix Expression (with spaces): ")
obj = PrefixEvaluation(expr)
result = obj.evaluate()
print("Result =", result)
