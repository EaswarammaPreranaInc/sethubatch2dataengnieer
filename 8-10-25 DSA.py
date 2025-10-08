Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
				                              --->  3 + (45*) - 6 / (27^)
				                              --->  3 + (45*) - (627^/)
				                              --->  (345*+) - (627^/)
				                              --->  345*+627^/-
    What  is  the  prefix  expression ?   --->
				                             ---> +3*45/6^27

2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> a ^ (bc^)
				                              --->  abc^^
    What  is  the  prefix  expression ?   --->
				                             ---> ^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  --->
				                              ---> ab+c+
    What  is  the  prefix  expression ?  --->
				                             ---> ++abc

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  --->
				                              ---> b2^4a*c*-0.5^-b+2a*/
    What  is  the  prefix  expression ?   --->
				                             ---> / + -b ^ - ^ b 2 * * 4 a c 0.5 * 2 a

5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  --->
				                              ---> ab<bc>cd<&
    What  is  the  prefix  expression ?   --->
				                             ---> 

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  --->
				                              ---> xy^5z*/2+
    What  is  the  prefix  expression ?   --->
				                             ---> + / ^ x y * 5 z 2

7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  --->
				                              ---> abcd^e-fgh*+^*+i-
    What  is  the  prefix  expression ?   --->
				                             ---> - + a * b ^ - ^ c d e + f * g h i





'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from stack import stack
def  icp(operator):
	# return  1  when  operator  is   +  (or)  -
	if operator in ['+' , '-']:
		return 1
	# return  2  when  operator  is   * , /   (or)  %
	elif operator in ['*' , '/' , '%']:
		return 2
	# return  4  when  operator  is   (  (or)  ^
	elif operator in ['(' , '^']:
		return 4
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
	# return  1  when  operator  is   +  (or)  -
	if operator in ['+' , '-']:
		return 1
	# return  2  when  operator  is   * , /   (or)  %
	elif operator in ['*' , '/' , '%']:
		return 2
	# return  3  when  operator  is   ^
	elif operator in ['^']:
		return 3
	# return  0  when  operator  is   (
	elif operator in ['(']:
		return 0
	# return  -1  when  operator  is  #
	elif operator in ['#']:
		return -1
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  ---> -1
'''
def  convert(infix):
	s = stack() # How  to  create  stack  class  object
	s . push('#') # How  to  push  '#'  into  the  stack
	postfix = '' # How  to  initialize  a  postfix  object  with  an  empty  string
	for x in infix : # How  to  iterate  infix  expression  with  for  loop:
		if  ch.isalnum() : # char  is  an  operand:
			postfix += ch # How  to  concatenate  the  operand  to  postfix  expression
		elif  ch == ')' # char  is  ')':
			while s.peek() != '(':
                		postfix += s.pop() # How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '('  becomes  last  element  of  stack
            		s.pop() # How  to  remove  '('   from  stack  but  do  not  concatenate  to  postfix  expression
		else:
			if   icp(operator)  >  isp(s.peek()): # (last-element-of-stack):
					s.push(char) # How  to  push  the  operator  into  the  stack
			else:
					# How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  icp > isp
					while icp(char) <= isp(s.peek()):
						postfix += s.pop()
					s.push(char) # How  to  push  the  operator  into  the  stack  when  icp > isp
	#  End  of  for  loop
	# How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '#'  becomes  last  element  of  stack
	while s.peek() != '#':
		postfix += s.pop()
	return postfix # How  to   return  postfix  expression
#  End  of  the  function
infix = input('Enter a Expression : ') # How  to  read  infix  expression
postfix = convert(infix) # How  to  convert  infix  expression  to  postfix expression
print(f'Postfix  expression  :  {postfix}') # How  to  print  postfix  expression




'''
Write  a  program  to  evaluate  postfix  expression

Posifix  expression  --->    345*+62/-
'''
from stack import stack
def  eval(a):
	s = stack() # How  to  create  a  stack  class  object
	for ch in postfix: # How  to  iterate  postfix  expression  with  for  loop:
		if char.isdigit():   # if the char is an operand
			s.push(int(char)) # How  to  push  the  operand  into  the  stack
				
		else:
			# How  to  remove  two  values  of  the  stack
			op2 = s.pop()
			op1 = s.pop()
			# match  the  operator  of  postfix  expression:
			# case   '+':  How to  push  addition  result  into  the  stack
			# case   '-':  How to  push  subtraction  result  into  the  stack
			# case   '*':  How to  push  product  result  into  the  stack
			# case   '/':  How to  push  division  result  into  the  stack
			# case   '^':  How to  push  power  result  into  the  stack	
			if char == '+':
				s.push(op1 + op2)  
			elif char == '-':
				s.push(op1 - op2) 
			elif char == '*':
				s.push(op1 * op2) 
			elif char == '/':
				s.push(op1 / op2)
			elif char == '^':
				s.push(op1 ** op2)

	#  End  of  for  loop
	return s.pop() # result  of  expression
#  End  of  the  function
infix = input('Enter infix expression: ') # How  to  read  infix  expression
from hw2 import convert
postfix = convert(infix) # How  to  convert infix  to  postfix
# How  to  evaluate  postfix  expression
result = eval(postfix)
print(f'Result : {result}')
