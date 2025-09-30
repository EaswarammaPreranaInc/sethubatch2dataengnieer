#  cal . py
_all_ =  ['add' , 'x'  , 'mul' , 'c1' , 'z']
x = 100
y = 200
def  add(a , b):
	return   a + b
def	  sub(a , b):
	return   a - b
def	  mul(a , b):
	return   a * b
def	  div(a  ,  b):
	return  a / b
class   c1:
	def  m1(self):
		print('m1  method')


'''
_all_
----------
1) What  is   _all_ ?  ---> List  of  members  of  the  module  which  are  to  be  imported  when  *  is  used

2) from  cal   import   *
    Which  members  are  imported ?  ---> Those  members  which  are  in  _all_  list  of  cal  module

3) What  happens  when  _all_  list  has  an  invalid  member ?  --->  from  module  import  *  throws  ImportError

4) Where  is  _all_  list  defined  ?  ---> Inside  the  module  i.e.  Any  where  in  the  module

5) from  cal   import   *
    Which  members  are  imported  when  _all_  list  is  not  defined  in  cal  module ?  --->
										All  the  members  are  imported  becoz  default  _all_  is   every  member  of  the  module

6) from  cal   import   *
    Which  members  are  imported  when  _all_  list  is  empty  in  cal  module ?  --->  No  member  is  imported

7) from  cal  import   y , sub , mul
    Which  members  are  imported ? ---> y , sub  and  mul  but  not  members  of  _all_  list

8) _all_  list  plays  a  key  role  only  when  *  is  used  in  import  clause  of  from  statement

9) import  module
    Which  members  are  imported ?  ---> No  member  is  imported  becoz  import  statement  imports  module  but  not  members
'''
