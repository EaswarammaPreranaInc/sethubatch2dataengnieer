'''
Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
  
# from  stack  import  Stack
'''
Write  a  program  to  convert  infix  to  prefix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from numpy import stack


def  icp(operator):
    if operator in '+-':
        return 2 # return  1  when  operator  is   +  (or)  -
    if operator in '*/%':
        return 3 # return  2  when  operator  is   * , /   (or)  %
    if operator == '^':
        return 4
    if operator in ')':
        return 5 # return  4  when  operator  is   (  (or)  ^
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
            return 4
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
    prefix = ''
    infix = infix[::-1]
    
    for char in infix:
        if char.isalnum():
            prefix += char
        elif char == ')':
            while s.peek() != '(':
                prefix += s.pop()
            s.pop()
            
        else:
            if icp(char) > isp(s.peek()):
                s.push(char)
            else:
                while icp(char) <= isp(s.peek()):
                    prefix += s.pop()
                s.push(char)
    while s.peek() != '#':
        prefix += s.pop()
    return prefix[::-1]
                
if __name__ == '__main__':
                       
    infix = input('Enter Infix expression : ')
    prefix = convert(infix)
    print('prefix expression :', prefix)
        
            














'''
Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''