'''
Write  a  program  to  perform  parentheses  match

1) Is  ((3 + 4)  valid ?  ---> No  due  to  excess  (

2) Is  (3 * (4 + 5))  valid ?  --->  Yes

3) Is  (3 * (4 + 5))) + 6 valid ? --->No  due  to  excess  ')'

4) Is  3 + 4  valid ? --->  Yes

5) Is  ) 3 + 4 (  valid ?  --->  No  due  to  )  before  (

6) What  action  to  be  made  when  character  is   '(' ?  --->  Push  '('  into  the  stack

7) What  action  to  be  made  when  character  is   ')' ?  ---> Pop  '('  from  the  stack

8) What  action  to  be  made  when  pop()  method  returns   None ?  --->  Print  invalid  msg  and  stop  execution

9) What  action  to  be  made  when  end  of   the  string   is  reached ? --->
																						Print  valid  msg  when  stack  is   empty  and  invalid  otherwise

10) Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from stack_implementation import stack
def paranthesis_match(str):
    s = stack() 
    for ch in str: 
        if ch == '(': 
            s.push(ch) 
        elif ch == ')': 
            if s.pop() == None:  
                print("Invalid: Excess ')' found")
                return
   
    if s.isempty():  
        print("Valid: All parentheses are matched")
    else:
        print("Invalid: Excess '(' found")


str = input("Enter a string with parentheses: ")
paranthesis_match(str)