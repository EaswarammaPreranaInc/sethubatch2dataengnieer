'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

a = input("Enter a string : ")
b = [a.upper()]
b.sort()
for b in ( 'A' , 'E' , 'I' , 'O' , 'U' ):
	count = count(b)
	print(f'{b} , {count}')




# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) 
print(b) # [ 'Y' : Yellow , ('G' , 'Gray'), ('R' , 'Red') , ('B' , 'Blue') ]
a . update(b) # Error Due to no update method in list class




#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a) 
print(b) # { (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90) }
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b) # { (10,) , (20,) , (30,) }




#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) # { 0 , 1 , 8 , 27 , 64 }
print(type(d)) # < class 'dict' >




# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) # { 0 , 2 , 4 , 6 , 8 }




# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # { 15 : 'Sita' , 17 : 'Kiran' }
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # { 10 : 'Rama' , 18 : 'Rajesh' , 12 : 'Rama Rao' }



# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') # Begin
x = f1() 
print(x) # 'Hyd' <next line> 'Sec' <next line> 'Cyb' < next line >  None < next line >
print(type(x)) # < class 'Nonetype' >
print('End') # End



# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1() 
print(x) # ( 10 , 20 , 30 )
print(type(x)) # < class tuple >
a , b , c =  f1()
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop')
for  k   in   f1():
	print(k) # 10 < new line > 20 < new line > 30 <new line >




# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin') # Begin
x = f1() 
print(x) # 10
print('End') # End
return   100 # Error 





#  Find  outputs
f1()
def   f1():
        print('Hello')
print(f1()) # Hello
print(f1) # < function f1 , address of f1




# Find  outputs  (Home  work)
print('Hello') # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # Hi
print(f1()) # f1 function < next line > None
print(f1) # < function f1 , address of function f1
print('Bye') # 'Bye'




#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # 'Begin'
print(type(f1)) # None type
print(id(f1)) # address of function f1
print('End') # End




#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20)) # 30
print(add('Hyder' , 'abad')) # Hyderabad
print(add(10.8 , 20.6)) # 31.4
print(add(True , False)) # 1
print(add(3 + 4j , 5 + 6j)) # ( 8 + 10j)
print(add(25 , 10.8)) # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) # [25 , 10.8 , 'Hyd' , True , None , 3+4j , 'Sec']
print(add(10 , '20')) #  Error







# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Three  argument  function :  10 , 20 , 30
f1(40 , 50) # Error
f1(60) # Error
f1() # Error





'''
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  ---> A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? ---> i =   2 , 3 , 4 , 5 , 6 , .....  12

3) Let  input   be  11
    What  is   the  range  of  divisors ? ---> i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  --->  return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
'''
def   prime(n):
	if a != int():
		print('Invalid input')
	elif a <= 1:
		return "Composite Number"
	elif a is prime number:
        for i range ( 2 , (a // 2) +1 ):
			if a % i == 0:
        return 'Composite Number'
    else:
		return "Prime Number"
a = int(input("Enter a number to know it is prime or not : "))
	
	return  true   when  'n'  is  prime  number  and  False  otherwise
'''
1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->

2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->

3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->

4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->
'''
How  to  read  a  number
if   input  is  invalid:
	print('Invalid  input')
elif  input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')
	





# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) # Emp Number  :  25 \t  Emp Name  :  Rama Rao \t  Salary  :  10000.0
disp('Sita' , 20000.0 , 35) # Emp Number  :  Sita \t  Emp Name  :  20000.0 \t  Salary  :  35



