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
if  __name__ ==  '__main__':
	print('Hyd')
	print('Sec')
	print('Cyb')
#hyd 
Sec
Cyb



#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
The modules and stats of system,time,math are imported
print()
print()
print(dir(time))
print()# all members and environment variables of time are imported 
print(dir(math))
# all members and environment variables of math are imported 




 #  Find  outputs  (Home  work)
import  cal
print(dir(cal))
#add
Sub
Mul
Div
C1 is imported and also __name__ is imported 


#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())#all members of current module is disp,class c1,__name__
print(type(dir()))#class function 
print(type(dir))# class list

 #  Find  outputs
print(dir())#error
print()#
import  cal
print()
print(dir())# error


 #  Find  outputs
print(dir())#error
print()
from  cal  import  *
print()
print(dir())# all members,statements are imported
#  Find  outputs
print(dir())#error
print()
from  cal  import  add , mul , x
print()
print(dir())#add ,mul,x and __name__

 # sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))#5
#import  cal
#cwd
standard libraries




from  random  import  *
print(random())#between 0&1
print(randint(1 , 100))#1&100
print(uniform(1 , 100))#any number inclusive of 1&100
print(randrange(10))#random numbers upto 10
print(randrange(1 , 11))between 1&11
print(randrange(1 , 11 , 2))between 1&11 with 2 steps
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))#any number in the list 
print(choice('RAJESH'))#any char in the string 
set  =  {10 , 20 , 30 , 40}
print(choice(set))#any number in the set 



# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
How  to  print  number  of  directories  (or)  folders  in  sys.path #len(sys.path)
How  to  append  c:\sairam  folder  to  sys.path# sys.path.append(c:\\sairam)
How  to  print  number  of  directories  (or)  folders  in  sys.path#len(sys.path)
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder#print(x)
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder#sairam.f1()
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder#a=sairam.c1()
A.m1()


1)from random import *

a={
0:"scissor",
1:"rock",
2:"paper"
}
op=int(input("what do you want to select(0-scissor,1-rock,2-paper): "))
com=randrange(1,4)
print(f"computer turn-{com} {a[com]}")
if op<3:
   if a[op]==a[com]:
       print("Its a draw")
   elif (com==1 and op==0) or (com ==0 and op==2) : 
        print("computer won")
   else:
       print("user won")
else:
   print("invalid input")


2)
import time
from random import*
list=["google.com","rediff.com","gmail.com","amazon.com","netflix.com"]

for i in range(len(list)):
    print(open(choice(list)))
    time.sleep(1.5)

3)from random import *
for i in range(10):
    print(randrange(123456,679926))
    
4)
from random import *
a=(2,3,4,5,6)
b=('a','b','c','d','e')
for i in range(10):
    passw=""
    for j in range(6):
       if j%2==0:
          passw += choice(b)
       else:
          passw += choice(a)
    print(passw)

5)
from random import *
a=input("enter a string: ")
for i in range(10):
   print(choice(a))
enter a string: Rama Rao
a
m
a
R
a
a
a

m
a

6)
from random import *
a=eval(input("enter list: "))
for i in range(10):
   print(choice(a))
enter list: ['hyd',None,123,3+4j]
hyd
None
123
None
hyd
123
hyd
hyd
(3+4j)
123
