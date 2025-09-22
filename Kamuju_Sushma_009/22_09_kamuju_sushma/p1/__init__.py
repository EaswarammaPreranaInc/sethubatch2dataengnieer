# Save  in   cwd \ p1 \ __init__ . py
print('__init__   module  of  package ' , __name__ , ' is  executed')
x = 10
def   f1():
	print('package  p1 ---> __init__  module ---> f1  function')
class   c1:
	def  m1(self):
		print('package  p1 ---> __init__  module ---> class  c1  ---> m1  method')


'''
1) What  is  the  name  of  module ?  ---> p1 . __init__

2) What  are  the  members  of  the  p1 . __init__ ?   ---> Object  'x'  ,  function   f1()  and  class   c1

3) py  __init__ . py
    What  are  the  outputs  ?  --->  __init__   module  of  package  __main__  is  executed
'''