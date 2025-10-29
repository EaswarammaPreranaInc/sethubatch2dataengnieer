'''

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

Write  a  program  to  evaluate  postfix  expression

Posifix  expression  --->    3 4 5 * + 6 2 / -



'''

from numpy import stack
import infix_to_postfix
# import stack  from numpy


def  eval(postfix):
    s = stack()
    for char in postfix:
        if char.isdigit():
            s.push(int(char))
        else:
            y = s.pop()
            x = s.pop()
            match char:
                case '+':
                    s.push(x + y)
                case '-':
                    s.push(x - y)
                case '*':
                    s.push(x * y)
                case '/':
                    s.push(x / y)
                case '^':
                    s.push(x ** y)
    return s.pop()           
'''       
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

'''
