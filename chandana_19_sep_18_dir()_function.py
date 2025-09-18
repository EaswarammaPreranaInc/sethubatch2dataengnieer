# cal.py
def  add(a , b):
	return  a + b
def  sub(a , b):
	return  a - b
def  mul(a , b):
	return  a * b
def  div(a , b):
	return  a / b
class    c1:
	def    m1(self):
		pass
#End  of  the  class
x = 100
y = 200
if  __name__ ==  "__main__":
	print('Hyd')
	print('Sec')
	print('Cyb')
'''
o/p:
Hyd
Sec
Cyb
'''



#  Find  outputs  
import  sys , time , math
print(dir(sys)) # gives all the members of the sys module and environmental variables in the form of list of strings
print()
print()
print(dir(time)) # gives all the members of the time module and environmental variables in the form of list of strings
print()
print(dir(math)) # gives all the members of the math module and environmental variables in the form of list of strings



#  Find  outputs  
import  cal
print(dir(cal)) # gives members of the cal module in the form of list of strings



#  Find  outputs  
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir()) # gives the members of the current module and environmental variables in the form of list of strings
print(type(dir())) # <class 'list'>
print(type(dir)) # <class 'builtin_function_or_method'>



'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '__name__' . startswith('__')  ?  ---> True

2) What  is  the  result  of  '__spec__' . endswith('__')  ?  --->  True

3) What  is  the  result  of  '__spec__' . startswith('__')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal
a=[]
for i in dir(cal):
	if not (i.startswith("__") and i.endswith("__")):
		a.append(i)
print(a)



#  Find  outputs
print(dir()) # gives the members of the current module and environmental variables in the form of list of strings
print()
import  cal
print()
print(dir()) # gives the members of the current module, imported modulename  and  environmental variables in the form of list of strings



#  Find  outputs
print(dir()) # gives the members of the current module and environmental variables in the form of list of strings
print()
from  cal  import  *
print()
print(dir())  # gives the members of the current module, imported module members  and  environmental variables in the form of list of strings



#  Find  outputs
print(dir()) # # gives the members of the current module and environmental variables in the form of list of strings
print()
from  cal  import  add , mul , x
print()
print(dir()) # gives the members of the current module, imported module members  and  environmental variables in the form of list of strings



# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path: # [cwd,python313.zip,Dils,lib,python313,site-packages]
	print(x)
print(len(sys . path)) # 6
#import  cal



# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  
import sys
print(len(sys.path)) #   print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam') #  append  c:\sairam  folder  to  sys.path
print(len(sys.path)) # print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x) #  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
print(sample.f1()) #   call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a=sample.c1()
a.m1()#   call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder


