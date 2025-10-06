'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
#How  to  import  stack  class  from  prog1b  module
from stack_implementation import stack
#How  to  create  stack  class  object
s = stack()
#How  to  read  a  string  into  a  str  object
str = input("Enter  a  string  :  ")
#How  to  push  each  char  of  string  into  the  stack
for  ch  in  str:
    s.push(ch)
print("Reverse  String :  ")
#How  to  remove  each  char  of  stack  and  print  until   stack  is  empty
while  not  s.isempty():
    print(s.pop(), end = '')
#End  of  while