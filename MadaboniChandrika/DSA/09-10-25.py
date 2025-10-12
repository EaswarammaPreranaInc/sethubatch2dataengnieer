#1st program
'''
Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
from prog1b import stack 
def icp(operator):
    if operator in '+-':
        return 2
    if operator in '*/%':
        return 3
    if operator == '^':
        return 4
    if operator == ')':
        return 5
def isp(operator):
    match operator:
        case '+' | '-':
            return 1
        case '*' | '/' | '%':
            return 2
        case '^':
            return 4
        case ')':
            return 0
        case '#':
            return -1
def convert(infix):
	infix=infix[::-1]
    s=stack()
	s.push('#')
	prefix=""
	for i in infix:
		if  i.isdigit():
			postfix+=i
		elif  i ==  '(':
			while s.peek!=")":
				x=s.pop()
				prefix+=x  
			s.pop()
		else:
			while icp(i)<=isp(s.peek()):
					prefix+=s.pop()
                    s.push(i)
	while s.peek()!='#':
		prefix+=s.pop()
    return prefix[::-1]
#  End  of  the  function
infix=input("Enter any infix expression : ")
prefix=convert(jnfix)
print(prefix)


#2nd program
'''
Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''
from prog9b import *
def  eval(prefix):
	s=stack()#How  to  create  a  stack  class  object
	for ch in prefix:#How  to  iterate  postfix  expression  with  for  loop:
		if  ch.isdigit():
				s.push(int(ch))#How  to  push  the  operand  into  the  stack
		else:
				x=s.pop()
				y=s.pop()#How  to  remove  two  values  of  the  stack
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
prefix=eval(infix)#How  to  convert infix  to  postfix
print(eval(prefix))#How  to  evaluate  postfix  expression