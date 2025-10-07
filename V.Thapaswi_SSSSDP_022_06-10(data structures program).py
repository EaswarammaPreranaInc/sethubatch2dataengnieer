'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from stack import stack # How  to  import  stack  class  from  prog1b  module
s=stack() # How  to  create  stack  class  object
a=input('Enter a string :') # How  to  read  a  string  into  a  str  object
for x in a:
    s.push(x) # How  to  push  each  char  of  string  into  the  stack
print("Reverse  String :",end='')
while not s.isempty():
    print(s.pop(),end='') # How  to  remove  each  char  of  stack  and  print  until   stack  is  empty



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
from stack import stack 
s=stack()
a=input('Enter expression :')
for x in a:
    if x=='(':
        s.push(x)
    elif x==')':
        if s.pop() is None:
            print('inValid')
            break
else:
    if s.isempty():
        print('valid')
    else:
        print('Invalid')
