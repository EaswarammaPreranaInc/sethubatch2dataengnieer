'''
Write  a  program  to  convert  infix  to  prefix
Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
from  stack  import   stack   #  Imports  stack  class  and  the  if  statements  outside stack  class
def  icp(operator):
	if  operator   in   '+-':
		return  2  #  icp  of  '+'  and  '-'  is   2
	if  operator   in   '*/%':
		return  3  #  icp  of  '*' ,  '/'   and  '%'  is   3
	if  operator  ==  '^':
		return  4
	if  operator  ==  ')':
		return  5
'''
icp('+')  --->   2
icp('*')  --->  3
icp('^')  --->  4
icp(')')  --->  5
'''
def  isp(operator):
	match  operator:
		case   '+' | '-':
			return  1
		case   '*' | '/' | '%':
			return  2
		case   '^':
			return  4
		case   ')':
			return  0
		case   '#':
			return  -1
'''
isp('-')  --->  1
isp('/')  --->  2
isp('^')  --->  4
isp(')')  --->  0
isp('#')  --->  -1
'''
def  convert(infix):
		infix = infix[::-1]  #  Reverses  infix  expression
		s = stack()
		s . push('#')
		prefix = ''
		for  ch  in  infix:
			if  ch . isdigit():
					prefix += ch
			elif  ch  ==  '(':
					while  s . peek()  !=  ')':
							prefix  += s.pop()
					s . pop()
			else:
					while   icp(ch)  <=  isp(s . peek()):
							prefix  += s . pop()
					s . push(ch)
        # End of  for  loop
		while  s . peek() != '#':
				prefix  +=  s . pop()
		return  prefix[::-1]  #  Reverse  the  result  to  obtain  prefix
# End  of  the  function
if  __name__ == '__main__':
        infix = input('Enter Infix expression : ')
        prefix = convert(infix)
        print('Prefix expression : ' ,  prefix)

'''
Write  a  program  to  evaluate  prefix  expression
Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''
from  stack  import  *
def  eval(prefix):
		prefix = prefix[::-1]  #  Reverses  prefix  expression
		s = stack()
		for  ch  in  prefix:
			if  ch . isdigit():
					s . push(int(ch))
			else:
					x = s . pop() #  1st  deleted  element  is  the  1st  operand
					y = s . pop()  #  2nd   deleted  element  is  the  2nd  operand
					if ch == '+':
						s . push(x + y)
					elif ch == '-':
						s . push(x - y)
					elif ch == '*':
						s . push(x * y)
					elif ch == '/':
						s . push(x // y)
					elif ch == '^':
						s . push(x ** y)
        # End of  for  loop
		return  s . pop()
# End of the  function
infix = input('Enter infix expression : ')
prefix = convert(infix)
print('Result : ' , eval(prefix))