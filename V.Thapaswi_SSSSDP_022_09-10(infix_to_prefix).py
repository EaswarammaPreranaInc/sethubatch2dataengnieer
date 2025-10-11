#Write  a  program  to  convert  infix  to  prefix

from stack import stack
def  icp(operator):
	if operator in '+-':
		return 2     # return  2  when  operator  is   +  (or)  -
	if operator in '*/%':
		return 3     # return  1  when  operator  is   * , /   (or)  %
	if operator == '^':
		return 4     # return  4  when  operator  is   ^
	if operator == ')':
		return 5  # return  5  when  operator  is   )

def  isp(operator):
	match operator:
		case '+' | '-':
			return 1 # return  1  when  operator  is   +  (or)  -
		case '*' | '/' | '%':
			return 2 # return  2  when  operator  is   * , /   (or)  %
		case '^':
			return 4 # return  4  when  operator  is   ^
		case ')':
			return 0 # return  0  when  operator  is   )
		case '#':
			return -1 # return  -1  when  operator  is  #
		
def  convert(infix):
	s=stack() 
	infix=infix[::-1]
	s.push('#') 
	prefix='' 
	for x in infix: 
		if  x.isalnum(): 
			prefix+=x 
		elif  x  ==  '(':
			while s.peek()!=')':
				prefix+=s.pop() 
			s.pop()
		elif icp(x) > isp(s.peek()):
			s.push(x) 
		else:
			while icp(x) <= isp(s.peek()): 
				prefix+=s.pop()
			s.push(x)
	while s.peek() != '#':
		prefix+=s.pop()
	return prefix[::-1]

if __name__=='__main__':
    infix=input("Enter infix expression :")
    prefix=convert(infix)
    print('Prefix expression :',prefix)