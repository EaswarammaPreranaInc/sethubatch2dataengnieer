  
# from  stack  import  Stack
'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from numpy import stack


def  icp(operator):
    if operator in '+-':
        return 1 # return  1  when  operator  is   +  (or)  -
    if operator in '*/%':
        return 2 # return  2  when  operator  is   * , /   (or)  %
    if operator in '()':
        return 4 # return  4  when  operator  is   (  (or)  ^
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
    match operator:
        case '+' | '-':
            return 1
        case '*' | '/' | '%':
            return 2
        case '^':
            return 3
        case '(':
            return 0
        case '#':
            return -1
# 	return  1  when  operator  is   +  (or)  -
# 	return  2  when  operator  is   * , /   (or)  %
# 	return  3  when  operator  is   ^i
# 	return  0  when  operator  is   (
# 	return  -1  when  operator  is  #
# '''


# isp('-')  --->  1
# isp('*')  --->  2
# isp('^')  --->  3
# isp('(')  --->  0
# isp('#')  ---> -1


def  convert(infix):
    s = stack()
    s.push('#')
    postfix = ''
    for char in infix:
        if char.isalnum():
            postfix += char
        elif char == ')':
            while s.peek() != '(':
                postfix += s.pop()
            s.pop()
            
        else:
            if icp(char) > isp(s.peek()):
                s.push(char)
            else:
                while icp(char) <= isp(s.peek()):
                    postfix += s.pop()
                s.push(char)
    while s.peek() != '#':
        postfix += s.pop()
    return postfix
                
if __name__ == '__main__':
                       
    infix = input('Enter Infix expression : ')
    postfix = convert(infix)
    print('Postfix expression :', postfix)
        
            

         
'''
	How  to  create  stack  class  object
	How  to  push  '#'  into  the  stack
	How  to  initialize  a  postfix  object  with  an  empty  string
	How  to  iterate  infix  expression  with  for  loop:
		if  char  is  an  operand:
			How  to  concatenate  the  operand  to  postfix  expression
		elif  char  is  ')':
			How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '('  becomes  last  element  of  stack
			How  to  remove  '('   from  stack  but  do  not  concatenate  to  postfix  expression
		else:
			if   icp(operator)  >  isp(last-element-of-stack):
					How  to  push  the  operator  into  the  stack
			else:
					How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  icp > isp
					How  to  push  the  operator  into  the  stack  when  icp > isp
	#  End  of  for  loop
	How  to  remove  each  element  of  stack  and  concatenate  to  postfix  expression  until  '#'  becomes  last  element  of  stack
	How  to   return  postfix  expression
#  End  of  the  function
How  to  read  infix  expression
How  to  convert  infix  expression  to  postfix expression
How  to  print  postfix  expression
'''


