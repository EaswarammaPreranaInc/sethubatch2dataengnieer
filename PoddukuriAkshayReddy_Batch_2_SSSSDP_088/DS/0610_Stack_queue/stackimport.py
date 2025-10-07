
'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite

How  to  import  stack  class  from  prog1b  module
How  to  create  stack  class  object
How  to  read  a  string  into  a  str  object
How  to  push  each  char  of  string  into  the  stack
printf("Reverse  String :  ");
How  to  remove  each  char  of  stack  and  print  until   stack  is  empty

'''
from stack import stack

if __name__ == '__main__':
    s = stack()   #  How  to  create  stack  class  object
    str_input = input("Enter a string: ")  # How to read a string into a str object
    for char in str_input:
        s.push(char)  # How to push each char of string into the stack
    print("Reversed String: ", end="")
    while not s.isempty():  # How to remove each char of stack and print until stack is empty
        print(s.pop(), end="")
    print()

