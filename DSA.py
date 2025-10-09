#  Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  '))
	def  get2(self):
		self . y = int(input('Enter  any  number  :  '))
		self . z = int(input('Enter  any  number  :  '))
	def   compute(self):
		Test . x += 1
		self . y  += 1
		self . z  += 1
		self . x  += 1
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1()
a = Test()
b = Test()
c = Test()
a . get2()
b . get2()
c . get2()
a . compute()#
b . compute()#
c . compute()#
a . disp()#13 35 46
b . disp()#13 45 55
c . disp()#13 61 71
12#13
a.y=34 
a.z=45
b.y=43
b.z=54





class  c1:
    x = 1
    y = 2
    z = 3
    def add(x,y):
        c1.c=x+y
        print(c1.c)
print(c1.x,c1.y,c1.z)
c1.add(c1.x,c1.y) 
c=c1.__dict__
for key,value in c1.__dict__.items():
    if key.startswith("__") and key.endswith("__"):
           continue
    else:
      print(f"{key}:{value}" ,end=" ")










'''
# infix_to_postfix.py
'''
from stack import *  # reuse stack class from prog1b.py

# Incoming precedence
def icp(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/', '%'):
        return 2
    elif operator in ('(', '^'):
        return 4
    else:
        return 0

# In-stack precedence
def isp(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/', '%'):
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 0
    elif operator == '#':
        return -1
    else:
        return 0

# Function to convert infix → postfix
def convert(infix):
    s = stack()           # create stack object
    s.push('#')           # push '#' into stack
    postfix = ''          # initialize postfix as empty string

    for ch in infix:
        if ch.isdigit() or ch.isalpha():   # operand (digit or variable)
            postfix += ch
        elif ch == ')':                    # closing parenthesis
            v = s.pop()
            while v != '(':
                postfix += v
                v = s.pop()
        else:                              # operator or '('
            while icp(ch) <= isp(s.peek()):
                postfix += s.pop()
            s.push(ch)

    # pop remaining operators from stack
    v = s.pop()
    while v != '#':
        postfix += v
        v = s.pop()

    return postfix

# main program
infix = input("Enter infix expression: ")
val = convert(infix)
print("Postfix expression:", val)


from stack import *   # reuse stack class

def evaluate_postfix(postfix):
    s = stack()          # create stack
    for ch in postfix:
        if ch.isdigit():         # operand
            s.push(int(ch))
        else:                     # operator
            y = s.pop()
            x = s.pop()
            if ch == '+':
                s.push(x + y)
            elif ch == '-':
                s.push(x - y)
            elif ch == '*':
                s.push(x * y)
            elif ch == '/':
                s.push(x // y)   # integer division
            elif ch == '%':
                s.push(x % y)
            elif ch == '^':
                s.push(x ** y)
    return s.pop()                # final result

# main
postfix = input("Enter postfix expression: ")
result = evaluate_postfix(postfix)
print("Result of postfix expression:", result)
