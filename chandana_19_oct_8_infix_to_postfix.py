'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from chandana_19_oct_6_stack import stack
def  icp(operator):
	if operator in '+-':
		return 1     # return  1  when  operator  is   +  (or)  -
	if operator in '*/%':
		return 2     # return  2  when  operator  is   * , /   (or)  %
	if operator in '(^':
		return 4     # return  4  when  operator  is   (  (or)  ^
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
	match operator:
		case '+' | '-':
			return 1 # return  1  when  operator  is   +  (or)  -
		case '*' | '/' | '%':
			return 2 # return  2  when  operator  is   * , /   (or)  %
		case '^':
			return 3 # return  3  when  operator  is   ^
		case '(':
			return 0 # return  0  when  operator  is   (
		case '#':
			return -1 # return  -1  when  operator  is  #
		
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  ---> -1
'''
def  convert(infix):
	s=stack() #  create  stack  class  object
	s.push('#') #  push  '#'  into  the  stack
	postfix=' ' #  initialize  a  postfix  object  with  an  empty  string
	for x in infix: #  iterate  infix  expression  with  for  loop:
		if  x.isalnum(): # char  is  an  operand:
			postfix+=x #  concatenate  the  operand  to  postfix  expression
		elif  x  ==  ')':
			while s.peek()!='(':
				postfix+=s.pop()  #  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '('  becomes  last  element  of  stack
			s.pop()
		elif icp(x) > isp(s.peek()):
			s.push(x) #  remove  '('   from  stack  but  do  not  concatenate  to  postfix  expression
		else:
			while icp(x) <=isp(s.peek()): 
				postfix+=s.pop()
			s.push(x)
	while s.peek() != '#':
		postfix+=s.pop()
	return postfix

if __name__=='__main__':
    infix=input("Enter infix expression :")
    postfix=convert(infix)
    print('Postfix expression :',postfix)
