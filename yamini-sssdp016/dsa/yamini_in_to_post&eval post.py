'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from stack import stack
def  icp(operator):
	if operator in '+-':
		return  1   # when  operator  is   +  (or)  -
	elif operator in '*/%^':
		return  2   # when  operator  is   * , /   (or)  %
	elif operator in '^':
		return  4   # when  operator  is   ^
	
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
	match(operator):
		case '+'|'-':
			return  1
		case '*'|'/'|'%':
			return  2
		case '^':
			return  3
		case '(':
			return  0
		case '#':
			return -1
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  ---> -1
'''
def  convert(infix):
	s=stack()   #How  to  create  stack  class  object
	s.push('#')   #How  to  push  '#'  into  the  stack
	post=''   #How  to  initialize  a  postfix  object  with  an  empty  string
	for i in infix:#How  to  iterate  infix  expression  with  for  loop:
		if  i.isdigit():
			post+=i #How  to  concatenate  the  operand  to  postfix  expression
		elif  i ==')':
			post+=s.pop()   #How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '('  becomes  last  element  of  stack
			s.pop()   #How  to  remove  '('   from  stack  but  do  not  concatenate  to  postfix  expression
		else:
			if   icp(i)  >  isp(s.peek()):
					s.push(i)   #How  to  push  the  operator  into  the  stack
			else:
					while  icp(i)  <=  isp(s.peek()):
						post+=s.pop()   #How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  icp > isp
					s.push(i)   #How  to  push  the  operator  into  the  stack  when  icp > isp
	#  End  of  for  loop
	while  s.peek()!='#':
		post+=s.pop()   #How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '#'  becomes  last  element  of  stack
	return  post   #How  to   return  postfix  expression
#  End  of  the  function
infix=input('Enter  infix  expression : ')   #How  to  read  infix  expression
x=convert(infix)   #How  to  convert  infix  expression  to  postfix expression
print('Postfix  expression : ' , x)   #How  to  print  postfix  expression


'''
Write  a  program  to  evaluate  postfix  expression

Posifix  expression  --->    3 4 5 * + 6 2 / -
'''
from stack import stack
from inf_to_post import convert
def  eval(a):
	s=stack()   #How  to  create  a  stack  class  object
	for i in a: #How  to  iterate  postfix  expression  with  for  loop:
		if i.isdigit(): #How  to  check  whetherhe  char  is  an  operand:
				s.push(int(i))  #How  to  push  the  operand  into  the  stack
		else:
				y=s.pop()
				x=s.pop()   #How  to  remove  two  values  of  the  stack
				match  i:   # the  operator  of  postfix  expression:
					case   '+':  s.push(x+y)
					case   '-': s.push(x-y)     #How to  push  subtraction  result  into  the  stack
					case   '*':  s.push(x*y)   #How to  push  product  result  into  the  stack
					case   '/':  s.push(x/y)   #How to  push  division  result  into  the  stack
					case   '^':  s.push(x**y)  #How to  push  power  result  into  the  stack
	#  End  of  for  loop
	return s.peek()
#  End  of  the  function
infix=input('Enter  infix  expression : ')  #How  to  read  infix  expression
x=convert(infix)   #How  to  convert infix  to  postfix
print('Result : ' , eval(x))   #How  to  evaluate  postfix  expression