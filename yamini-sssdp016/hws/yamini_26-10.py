'''
Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer  to  prog8
'''

from datatype import string, number
try:
	s = input('Enter class name (string , number to join or add ) : ')  #   Reads  strint  class  name
	classname = eval(s) #   Converts  string  class  name  to  classname
	a = [classname(),classname(),classname()]  # Create 3 number objects
except:
	print('Invalid  class  name')
a[0].get()  # Read input into first object
a[1].get()  #  Read input into second object
a[2].add(a[0], a[1])  # Add/join and store in third object
a[2].display()  # Print result

