#Ramu(08-10)


'''
Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
				                              --->  3 + (45*) - 6 / (27^)
				                              --->  3 + (45*) - (627^/)
				                              --->  (345*+) - (627^/)
				                              --->  345*+627^/-
    What  is  the  prefix  expression ?   --->3 + 4 * 5 - 6 / (^27)
				                         --->3 + (*45) - 6 / (^27)
				                         --->3 + (*45) - /6^27
				                         --->(+3*45) - /6^27
				                         --->-+3*45/6^27
                            

2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> a ^ (bc^)
				                              --->  abc^^
    What  is  the  prefix  expression ?   --->a ^ b ^ c
				                             --->a^(^bc)
				                             --->^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  ---> ab+ + c
				                              --->ab+c+
    What  is  the  prefix  expression ?  --->+ab + c
				                             --->++abc

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  --->(-b + (b2^ - 4 * a * c) ^ 0.5) / (2 * a)
				                          --->(-b + (b2^ - 4a* * c) ^ 0.5) / (2 * a)
				                          --->(-b + (b2^ - 4a*c*) ^ 0.5) / (2 * a)
				                          --->(-b + (b2^4a*c*-) ^ 0.5) / (2 * a)
				                          --->(-b + (b2^4a*c*-) ^ 0.5) / (2 * a)
				                          --->(-b + b2^4a*c*-0.5^) / (2 * a)
				                          --->(-bb2^4a*c*-0.5^+) / (2 * a)
                                          ---->(-bb2^4a*c*-0.5^+) / 2a*
                                          ---->-bb2^4a*c*-0.5^+2a*/

What  is  the  prefix  expression ?   --->/+-b^-^b2**4ac0.5*2a
                                          
                                          

5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  --->ab<bc>cd< and or
    What  is  the  prefix  expression ?   --->or<ab and >bc<cd

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  --->xy^5Z*/2+
    What  is  the  prefix  expression ?   --->+/^xy*5z2
				                            

7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  --->abcd^e-fgh*+^*+i-
				                        
    What  is  the  prefix  expression ?   --->-+a*b^-^cde+f*ghi
				                    
 '''    
                    
'''
Write  a  program  to  convert  infix  to  postfix
Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from stack import stack
def  icp(operator):
    if operator=='+' or operator=='-':
        return 1 #return  1  when  operator  is   +  (or)  -
    elif operator=='*' or operator=='/' or operator=='%':
        return 2 #return  2  when  operator  is   * , /   (or)  %
    elif operator=='(' or operator=='^':
        return 4
     #return  4  when  operator  is   (  (or)  ^
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
    if operator=='+' or operator=='-':
        return 1 #return  1  when  operator  is   +  (or)  -
    elif operator=='*' or operator=='/' or operator=='%':
        return 2 #return  2  when  operator  is   * , /   (or)  %
    elif operator=='^':
        return 3
    elif operator=='(':
        return 0
    elif operator=='#':
        return -1
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  ---> -1
'''
def  convert(infix):
    s=stack()
    s.push('#')
    s.postfix='' 
    for char in infix:
        if  char.isalnum():
            s.postfix+=char
        elif  char  ==  ')':
            while not s.peek()=='(':
                x=s.pop()
                s.postfix+=x
            if s.peek()=='(':
                s.pop()
        else:
            if icp(char) > isp(s.peek()):
                s.push(char)
            else:
                while icp(char)<=isp(s.peek()):
                    x=s.pop()
                    s.postfix+=x
                if icp(char)>isp(s.peek()):
                    s.push(char)
    while not s.peek()=='#':
        x=s.pop()
        s.postfix+=x
    return s.postfix
#  End  of  the  function
if _name=='main_':
    infix=input("Enter infix Expression")#How  to  read  infix  expression
    postfix=convert(infix) #How  to  convert  infix  expression  to  postfix expression
    print('Postfix Expression :',postfix)
    

'''
Write  a  program  to  evaluate  postfix  expression

Posifix  expression  --->    3 4 5 * + 6 2 / -
'''
from infixtopostfix import convert
from stack import stack
def  eval(a):
    s=stack()
    for char in a:
        if  char.isalnum():
            s.push(int(char))
        else:
            y=s.pop()
            x=s.pop()
            match char:
                case   '+':  s.push(x+y)
                case   '-':  s.push(x-y)
                case   '*':  s.push(x*y)
                case   '/':  s.push(x//y)
                case   '^':  s.push(x**y)
    return  s.peek()
#  End  of  the  function
infix=input("Enter infix Expression : ")#How  to  read  infix  expression
postfix=convert(infix) #How  to  convert infix  to  postfix
result=eval(postfix)#How  to  evaluate  postfix  expression
print('Result : ',result)


