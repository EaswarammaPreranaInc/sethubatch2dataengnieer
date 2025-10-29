[08-10-2025 12:50] SRINIVAS Sir SSSSDP: Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
				                              --->  3 + (45*) - 6 / (27^)
				                              --->  3 + (45*) - (627^/)
				                              --->  (345*+) - (627^/)
				                              --->  345*+627^/-
    What  is  the  prefix  expression ?   --->
				                             --->

2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> a ^ (bc^)
				                              --->  abc^^
    What  is  the  prefix  expression ?   --->
				                            --->

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  --->
				                              --->
    What  is  the  prefix  expression ?  --->
				                             --->

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  --->
				                              --->
    What  is  the  prefix  expression ?   --->
				                             --->

5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  --->
				                              --->
    What  is  the  prefix  expression ?   --->
				                             --->

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  --->
				                              --->
    What  is  the  prefix  expression ?   --->
				                             --->

7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  --->
				                              --->
    What  is  the  prefix  expression ?   --->
				                             --->
[08-10-2025 13:22] SRINIVAS Sir SSSSDP: Conversion  of  Infix  to  Postfix
---------------------------------------
Operator          Icp(Incoming  priority)   Isp(In  stack  priority)
---------------------------------------------------------------------------
     + ,  -			1					1   --->  icp = isp  due  to  left  to  right  conversion

     * ,  / ,  %		2					2  --->  icp = isp  due  to  left  to  right  conversion

     ^			        4				        3   --->  icp > isp  due  to  right  to  left  conversion

     (				4					0

     #				-					-1
---------------------------------------------------------------------------
Let  infix  expression  be  3 + 4 * 5 - (6 + 7 * 8) / 9 + 2 * 5

    Character       Stack         Postfix  expression
-----------------------------------------------------------
                              #                    ''
          3                  #                    '3'
          +                  #+                   '3'
          4                 #+                   '34'
          *                 #+*                 '34'
          5                 #+*                 '345'
          -                 #-                    '345*+'
          (                 #-(                   '345*+'
          6                #-(                   '345*+6'
          +                #-(+                  '345*+6'
          7                #-(+                  '345*+67'
          *                #-(+*                '345*+67'
          8                #-(+*                '345*+678'
          )                #-                      '345*+678*+'
          /                #-/                    '345*+678*+'
          9                #-/                    '345*+678*+9'
          +                #+                      '345*+678*+9/-'
          2                #+                      '345*+678*+9/-2'
          *                #+*                    '345*+678*+9/-2'
          5                #+*                    '345*+678*+9/-25'
          End            #                        '345*+678*+9/-25*+'
          --------------------------------------------------------------
	Postfix  expression :  345*+678*+9/-25*+


1) Which  object  has  infix  expression  ?   ---> A  str  object
    Which  object  has  postfix  expression ? ---> Another  str  object

2) Why  is  '#'  pushed  into  the  stack   ?  --->  In  view  of  1st  comparison

3) What  action  to  be  made  when  character  is  operand(i.e. '0'  to  '9' )  ?  --->
														Concatenate  the  operand  to  postfix  expression

4) What  action  to  be  made  when  character  is  operator ? --->
									Compare  icp   of   the  operator  with  isp  of  last  element  of  the  stack

5) What  action  to  be  made  when  icp(operator) > isp(last-element-of-the-stack) ?  --->  Push  the  operator  into  the  stack

6) What  action  to  be  made  when  icp(operator)  <=  isp(last-element-of-the-stack)  ?  --->
					Pop  the  operator  from  the  stack  and  concatenate  the  deleted  operator  to  postfix  expression

7) How  long  is  the  deletion  continued ?  ---> Until  icp > isp

8) What  action  to  be  made  when  icp > isp ?  ---> Push  the  operator  into  the  stack

9) What  action  to  be  made  when  character  is  ')' ?  --->  Pop  the  operator  from  the  stack  and
											         concatenate  the  deleted  operator  to  postfix  expression

10) How  long  is  the  deletion  continued ?  --->  Until  '('  becomes  last  element  of  stack

11) What  action  to  be  made  when  '('  is  the  last  element  of  stack ?  --->
										Pop  '('   also  but  do  not  concatenate  '('  to  postfix  expression
										as  postfix  expression  is  bracket  free  expression

12) What  action  to  be  made  when  end  of  infix  expression  is  reached  ?  --->
												Pop  the  operator  from  the  stack  and
												concatenate  the  deleted  operator  to  postfix  expression

13) How  long  is  the  deletion  continued ?  --->  Until  '#'  becomes  last  element  of  stack

    
    
    
    
'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
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
    s = Stack()
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




 Evaluation  of  Postfix  Expression
----------------------------------------
1) Infix  :  3 + 4 * 5 - 6 / 2
    Postfix :  3 + (45*) - 6 / 2
                 :  3 + (45*) - (62/)
                 :  (345*+) - (62/)
                 :  345*+62/-

2)  character   Stack
   -----------------------
            '3'             '3'
            '4'              3 , 4
            '5'              3 , 4 , 5
            '*'              3 ,  4 * 5 = 20
            '+'              3 + 20 = 23
            '6'              23 , 6
            '2'              23 , 6 , 2
            '/'              23 , 6 / 2 = 3
            '-'              23 - 3 = 20

3) Which  object  has  postfix  expression ? ---> A  str  object

4) What  action  to  be  made  when  character  is  operand(i.e. '0'  to  '9' )  ?  ---> Push  int(operand)  into  the  stack

5) What  action  to  be  made  when  character  is  operator ? --->  Pop  the  last  two  elements  of  the  stack ,
													 save  them  in  'y'  and  'x'  and
													 push  the  result  of  x  operator  y  into  the  stack

6) What  does  stack  finally  contain ?  ---> Result  of  the  postfix  expression

7) Postfix  expression  is  bracket  free  expression
'''
Write  a  program  to  evaluate  postfix  expression

Posifix  expression  --->    3 4 5 * + 6 2 / -
'''
def  eval(a):
	How  to  create  a  stack  class  object
	How  to  iterate  postfix  expression  with  for  loop:
		if  the  char  is  an  operand:
				How  to  push  the  operand  into  the  stack
		else:
				How  to  remove  two  values  of  the  stack
				match  the  operator  of  postfix  expression:
					case   '+':  How to  push  addition  result  into  the  stack
					case   '-':  How to  push  subtraction  result  into  the  stack
					case   '*':  How to  push  product  result  into  the  stack
					case   '/':  How to  push  division  result  into  the  stack
					case   '^':  How to  push  power  result  into  the  stack
	#  End  of  for  loop
	return  result  of  expression
#  End  of  the  function
How  to  read  infix  expression
How  to  convert infix  to  postfix
How  to  evaluate  postfix  expression