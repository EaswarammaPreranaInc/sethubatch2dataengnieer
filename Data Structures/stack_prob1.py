'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from stack import stack
stack = stack()
string = input('Enter the word:  ')
for c in string:
    stack.push(c)
print('Reverse String:  ')
while not stack.isempty():
    print(stack.pop(), end='')


# How  to  create  stack  class  object
# How  to  read  a  string  into  a  str  object
# How  to  push  each  char  of  string  into  the  stack
# printf("Reverse  String :  ");
# How  to  remove  each  char  of  stack  and  print  until   stack is empty

