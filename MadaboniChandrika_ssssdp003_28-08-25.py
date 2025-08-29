
#1st program
a=input("Enter string:")
a=a.upper() #RAMA RAO
c={}
for x in a:
    if x in 'AEIOU':
        c[x]=a.count(x)
print(c)


#2nd program
# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)#{'Y' : 'Yellow', 'G' : 'Green', 'R' : 'Red', 'B' : 'Blue'}
a . update(b)#Error,list object has no attribute 'update'


#3rd program
#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)#Error,dict expected at most 1 argument, got 3
print(b)#{}
c = [(10,) , (20,) , (30,)]
b . update(c)#Error,dict expected at most 1 argument, got 3
print(b)#{}

#4th program
#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)#{0:0,1:1,2:8,3:27,4:64}
print(type(d))#<class 'dict'>

#5th program
# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)#{0:0,1:2,2:4,3:6,4:8}


#6th program
# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)#{15:'Sita',17:'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)#{10:'Rama',18:'Rajesh',12:'Rama Rao}'}

#7th program
# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')#Begin
x = f1()#Hyd \n Sec \n Cyb
print(x)#None
print(type(x))#<class 'NoneType'>
print('End')#End


#8th program
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()#(10,20,30)
print(x)#(10, 20, 30)
print(type(x))#<class 'tuple'>
a , b , c =  f1()
print(a)#10
print(b)#20
print(c)#30
print('for  loop')
for  k   in   f1():
print(k)#10 \n 20 \n 30


#9th program
# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')#Begin
x = f1()
print(x)#10
print('End')#End
#return   100#Error , return outside function

#10th program
#  Find  outputs
#f1()#Error function call before definition
def   f1():
        print('Hello')
print(f1())#Hello \n None
print(f1)#<function f1 at 0x000001E2B3C8A700>


#11th program
# Find  outputs  (Home  work)
print('Hello')#Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')#Hi
print(f1())#f1  function \n None
print(f1)#<function f1 at 0x000001E2B3C8A700>
print('Bye')#Bye

#12th program
#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')#Begin
print(type(f1))#<class 'function'>
print(id(f1))#some address
print('End')#End


#13th program
#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))#30
print(add('Hyder' , 'abad'))#Hyderabad
print(add(10.8 , 20.6))#31.4
print(add(True , False))#1
print(add(3 + 4j , 5 + 6j))#(8+10j)
print(add(25 , 10.8))#35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))#[25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))#Error , int and str cannot be added


#14th program
# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)#Three  argument  function :  10 20 30
#f1(40 , 50)#Error 
#f1(60)#Error
#f1()#Error

#15th program
def prime (n):
    if n > 1:
        for i in range(2,(n//2) + 1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False
n=int(input("Enter a number:"))
if  n<2:
	print('Invalid  input')
elif  prime(n):
	print('Prime  number')
else:
	print('Composite number')


#16th program
# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)#Emp  Number  :  25 	 Emp Name  :  Rama  Rao 	 Salary  :  10000.0
disp('Sita' , 20000.0 , 35)#Emp  Number  :  Sita 	 Emp Name  :  20000.0 	 Salary  :  35


