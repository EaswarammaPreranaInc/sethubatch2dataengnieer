'''
Write  a  program  to  convert  infix  to  prefix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''

from stack import stack

def icp(operator):
	if operator in '+-':
		return 2  # when operator is + or -
	elif operator in '*/%^':
		return 3  # when operator is * / % ^
	elif operator in '^':
		return 4  # when operator is ^
	elif operator in ')':
		return 5  # when operator is )
	
def isp(operator):
	match(operator):
		case '+'|'-':
			return 1
		case '*'|'/'|'%':
			return 2
		case '^':
			return 4
		case ')':
			return 0
		case '#':
			return -1

def infix_to_postfix(infix):
	s = stack()
	s.push('#')
	post = ''
	for i in infix:
		if i.isdigit() or i.isalpha():
			post += i
		elif i == '(':
			while s.peek() != ')':
				post += s.pop()
			s.pop()
		else:
			if icp(i) > isp(s.peek()):
				s.push(i)
			else:
				while icp(i) <= isp(s.peek()):
					post += s.pop()
				s.push(i)
	while s.peek() != '#':
		post += s.pop()
	return post

def convert(infix):
	# Step 1: Reverse the infix expression directly
	infix = infix[::-1]

	# Step 2: Convert reversed infix using same logic
	post = infix_to_postfix(infix)

	# Step 3: Reverse the result to get prefix
	pre = post[::-1]
	return pre

if __name__ == '__main__':
	infix = input('Enter infix expression: ')
	x = convert(infix)
	print('Prefix expression :', x)



from stack import stack
from inf_to_pre import convert
def  eval(a):
	s=stack()   
	for i in a: 
		if i.isdigit(): 
				s.push(int(i)) 
			
		else:
				x=s.pop()
				y=s.pop()  
				match  i:   
					case   '+':  s.push(x+y)
					case   '-': s.push(x-y)     
					case   '*':  s.push(x*y)   
					case   '/':  s.push(x/y)   
					case   '^':  s.push(x**y)  
	#  End  of  for  loop
	return s.peek()
#  End  of  the  function
infix=input('Enter  infix  expression : ')  #How  to  read  infix  expression
x=convert(infix)   #How  to  convert infix  to  prefix
print('Result : ' , eval(x))   #How  to  evaluate  prefix  expression

