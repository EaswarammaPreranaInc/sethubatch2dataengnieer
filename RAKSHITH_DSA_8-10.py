'''
Conversion
---------------------------------------------------------------------------------------
1) Let infix expression be 3 + 4 * 5 - 6 / 2 ^ 7
    Postfix expression 
    3 + 4 * 5 - 6 / 2 ^ 7
   ---> 3 + (45*) - 6 / 2 ^ 7
   ---> 3 + (45*) - 6 / (27^)
   ---> (3 + 45*) - (627^/)
   ---> 345*+627^/-

    Prefix expression 
    3 + 4 * 5 - 6 / 2 ^ 7
   ---> 3 + (4*5) - 6 / (2^7)
   ---> + 3 * 4 5 - 6 / ^ 2 7
   ---> - + 3 * 4 5 / 6 ^ 2 7

2) Let infix expression be a ^ b ^ c
    Postfix expression
    a ^ b ^ c
   ---> a ^ (b ^ c)
   ---> a (b c ^) ^
   ---> abc^^

    Prefix expression
    a ^ b ^ c
   ---> a ^ (b ^ c)
   ---> ^ a ^ b c

3) Let infix expression be a + b + c
    Postfix expression 
    a + b + c
   ---> (a + b) + c
   ---> (ab+) + c
   ---> ab+c+

    Prefix expression 
    a + b + c
   ---> (a + b) + c
   ---> + + a b c
   ---> ++abc

4) Let infix expression be (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    Postfix expression
    (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
   ---> (-b + ((b ^ 2) - (4*a*c)) ^ 0.5) / (2*a)
   ---> (-b + ((b 2 ^ 4 a * c * -) 0.5 ^)) / (2*a)
   ---> (b u- (b 2 ^ 4 a * c * - 0.5 ^) +) / (2 a *)
   ---> b u- 2 ^ 4 a * c * - 0.5 ^ + 2 a * /

    Prefix expression
    (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
   ---> u- b + (b ^ 2 - 4 * a * c) ^ 0.5
   ---> u- b + ^ ( - ^ b 2 * 4 a c) 0.5
   ---> / + u- b ^ - ^ b 2 * 4 a c 0.5 * 2 a

5) Let infix expression be a < b or b > c and c < d
    Postfix expression
    a < b or b > c and c < d
   ---> (a < b) or ((b > c) and (c < d))
   ---> (ab<) or ((bc>) (cd<) and)
   ---> ab< bc> cd< and or

    Prefix expression
    a < b or b > c and c < d
   ---> a < b or ((b > c) and (c < d))
   ---> < a b or ( > b c and < c d )
   ---> or < a b and > b c < c d

6) Let infix expression be x ^ y / (5 * z) + 2
    Postfix expression
    x ^ y / (5 * z) + 2
   ---> (x ^ y) / (5 * z) + 2
   ---> (xy^) / (5 z *) + 2
   ---> xy^ 5 z * / 2 +

    Prefix expression
    x ^ y / (5 * z) + 2
   ---> (x ^ y) / (5 * z) + 2
   ---> + / ^ x y * 5 z 2

7) Let infix expression be a + b * (c ^ d - e) ^ (f + g * h) - i
    Postfix expression
    a + b * (c ^ d - e) ^ (f + g * h) - i
   ---> a + b * ((c ^ d - e) ^ (f + g * h)) - i
   ---> a + b * ((cd^ - e) ^ (f + gh*)) - i
   ---> a + b * (cd^e- fgh* + ^) - i
   ---> a + b * cd^e-fgh*+^ - i
   ---> ab cd^e-fgh*+^ * + i -
   ---> abcd^e-fgh*+^*+i-

    Prefix expression
    a + b * (c ^ d - e) ^ (f + g * h) - i
   ---> a + b * ((c ^ d - e) ^ (f + g * h)) - i
   ---> + a * b ^ - ^ c d e + f * g h - i
   ---> - + a * b ^ - ^ c d e + f * g h i
'''


'''
Write  a  program  to  convert  infix  to  postfix
Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
# from prog1b import stack

def icp(operator):
    # in-coming precedence
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/' or operator == '%':
        return 2
    elif operator == '(' or operator == '^':
        return 4

def isp(operator):
    # in-stack precedence
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/' or operator == '%':
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 0
    elif operator == '#':
        return -1

def convert(infix):
    # How to create stack class object
    s = stack()
    
    # How to push '#' into the stack
    s.push('#')
    
    # How to initialize a postfix object with an empty string
    postfix = ''
    
    # How to iterate infix expression with for loop
    for char in infix:
        # if char is an operand
        if char.isalnum():
            # How to concatenate the operand to postfix expression
            postfix += char
        # elif char is ')'
        elif char == ')':
            # How to remove each element of stack and concatenate to postfix until '(' becomes last element
            while s.peek() != '(':
                postfix += s.pop()
            # How to remove '(' from stack but do not concatenate
            s.pop()
        else:
            # else (operator)
            while icp(char) <= isp(s.peek()):
                # How to remove each element of stack and concatenate to postfix until icp > isp
                postfix += s.pop()
            # How to push the operator into the stack when icp > isp
            s.push(char)
    
    # How to remove each element of stack and concatenate to postfix until '#' becomes last element
    while s.peek() != '#':
        postfix += s.pop()
    
    # How to return postfix expression
    return postfix
# End of the function

# How to read infix expression
infix = input("Enter infix expression: ")

# How to convert infix expression to postfix expression
postfix = convert(infix)

# How to print postfix expression
print("Postfix expression:", postfix)


'''
Write  a  program  to  evaluate  postfix  expression
Posifix  expression  --->    3 4 5 * + 6 2 / -
'''
# from prog1b import stack

def eval_postfix(postfix):
    # How to create a stack class object
    s = stack()
    
    # How to iterate postfix expression with for loop
    for char in postfix:
        # if the char is an operand
        if char.isdigit():  # for simplicity, assuming single-digit operands
            # How to push the operand into the stack
            s.push(int(char))
        else:
            # How to remove two values of the stack
            val2 = s.pop()
            val1 = s.pop()
            
            # match the operator of postfix expression
            if char == '+':
                # How to push addition result into the stack
                s.push(val1 + val2)
            elif char == '-':
                # How to push subtraction result into the stack
                s.push(val1 - val2)
            elif char == '*':
                # How to push product result into the stack
                s.push(val1 * val2)
            elif char == '/':
                # How to push division result into the stack
                s.push(val1 / val2)
            elif char == '^':
                # How to push power result into the stack
                s.push(val1 ** val2)
    # End of for loop
    
    # return result of expression
    return s.pop()
# End of the function

# How to read infix expression
infix = input("Enter infix expression: ")

# How to convert infix to postfix
# Assume convert() is defined from your previous program
postfix = convert(infix)

print("Postfix expression:", postfix)

# How to evaluate postfix expression
result = eval_postfix(postfix)
print("Result of expression:", result)




