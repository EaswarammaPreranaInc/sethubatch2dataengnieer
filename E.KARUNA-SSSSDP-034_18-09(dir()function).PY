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
if  __name__ ==  '_main_':
	print('Hyd')
	print('Sec')
	print('Cyb')




#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()#All the members of sys module and enviornment variables
print()
print(dir(time))
print()#All the members of time module and environment variables
print(dir(math))#All the members of math module and enviornment variables


#  Find  outputs  (Home  work)
import  cal
print(dir(cal))#['add','sub','mul','div','c1','x'x,'y' and enviornment variables]



#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())#members of the curreent model i.e['x','disp','c1'and environment variables]
print(type(dir()))#<class 'list'>
print(type(dir))#<class 'buitins function'>





#  Find  outputs
print(dir())#[environment variables]
print()
import  cal
print()
print(dir())##['cal and environment variables]



#  Find  outputs
print(dir())#[environment variables]
print()
from  cal  import  *
print()
print(dir())#['add','sub','mul','div','c1','x','y' and Environment Variables]





#  Find  outputs
print(dir())#[environment variables]
print()
from  cal  import  add , mul , x
print()
print(dir()) #['add','mul','x' and Environment Variables]





# sys . path  demo   program
import  sys
print('Original  sys.path')#Original sys.path
for  x  in   sys . path:
	print(x)#[cwd and 5 other standards directories]
print(len(sys . path))#6
#import  cal




# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
print(sys.path) #How  to  print  number  of  directories  (or)  folders  in  sys.path
sys.path.append('c:\\sairam') #How  to  append  c:\sairam  folder  to  sys.path
print(len(sys.path))#How  to  print  number  of  directories  (or)  folders  in  sys.path
import sample
print(sample.x)#How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
sample.f1()#How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a=sample.c1()
a.m1()#How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder




from  random  import  *
print(random()) # a number b/w 0 and 1 (excluding 0 and 1) i.e some random number 0.3
print(randint(1 , 100)) # a integer number b/w 1 and 100 (including 1 and 100)i.e 55
print(uniform(1 , 100)) # a float number b/w 1 and 100(including 1 and 100) i.e 23.5
print(randrange(10))#a integer number b/w 0 and 9 i.e 7
print(randrange(1 , 11)) # a integer number b/w 1 and 10 i.e 5
print(randrange(1 , 11 , 2))#a integer number b/w 1 and 10 in steps of 2 i.e some random number 6
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # a number from the list
print(choice('RAJESH')) # a character from sequence
set  =  {10 , 20 , 30 , 40}
print(choice(set)) #Error due set caanot support


