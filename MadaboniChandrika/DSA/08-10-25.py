#1st program
'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from prog1b import stack
def  icp(operator):
	if operator=='+' or operator=='-' :
		return 1#return  1  when  operator  is   +  (or)  -
	if operator=='*' or operator=='/' or operator=='%'  :
		return  2 
	if operator=='(' or operator=='^' :
		return  4 
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
	if operator=='+' or operator=='-' :
		return  1  
	if operator=='*' or operator=='/' or operator=='%'  :
		return  2  
	if operator=='^':
		return  3  
	if operator=='(':
		return  0  
	if operator=='#':
		return  -1  
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  ---> -1
'''
def  convert(infix):
	s=stack()#How  to  create  stack  class  object
	s.push('#')#How  to  push  '#'  into  the  stack
	postfix=""#How  to  initialize  a  postfix  object  with  an  empty  string
	for i in infix:#How  to  iterate  infix  expression  with  for  loop:
		if  i.isalnum():
			postfix+=i#How  to  concatenate  the  operand  to  postfix  expression
		elif  i ==  ')':
			while s.peek!="(":
				x=s.pop()
				postfix+=x#How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '('  becomes  last  element  of  stack
			s.pop()#How  to  remove  '('   from  stack  but  do  not  concatenate  to  postfix  expression
		else:
			if   icp(i)  >  isp(s.peek()):
					s.push(i)#How  to  push  the  operator  into  the  stack
			else:
					while icp(i)<=isp(s.peek()):
						postfix+=s.pop()#How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  icp > isp
					    s.push(i)#How  to  push  the  operator  into  the  stack  when  icp > isp
	#  End  of  for  loop
	while s.peek()!='#':#How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '#'  becomes  last  element  of  stack
		postfix+=s.pop()
	return postfix#How  to   return  postfix  expression
#  End  of  the  function
x=input("Enter any infix expression : ")#How  to  read  infix  expression
postfixexp=convert(x)#How  to  convert  infix  expression  to  postfix expression
print(postfixexp)#How  to  print  postfix  expression


#2nd program
'''
Write  a  program  to  evaluate  postfix  expression

Posifix  expression  --->    3 4 5 * + 6 2 / -
'''
from prog7b import *
def  eval(postfix):
	s=stack()#How  to  create  a  stack  class  object
	for ch in postfix:#How  to  iterate  postfix  expression  with  for  loop:
		if  ch.isdigit():
				s.push(int(ch))#How  to  push  the  operand  into  the  stack
		else:
				y=s.pop()
				x=s.pop()#How  to  remove  two  values  of  the  stack
				match  ch :
					case   '+':  
						s.push(x+y)#How to  push  addition  result  into  the  stack
					case   '-':  
						s.push(x-y)#How to  push  subtraction  result  into  the  stack
					case   '*':  
						s.push(x*y)#How to  push  product  result  into  the  stack
					case   '/': 
						s.push(x//y)# How to  push  division  result  into  the  stack
					case   '^':  
						s.push(x**y)#How to  push  power  result  into  the  stack
	#  End  of  for  loop
	return  s.pop()
#  End  of  the  function
infix=input("Enter the infix exp: ")#How  to  read  infix  expression
postfix=eval(infix)#How  to  convert infix  to  postfix
print(eval(postfix))#How  to  evaluate  postfix  expression