'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
s = input('Enter String:') #   Reads  a  string
s = s . upper()  #  Returns  uppercase  string
vowels = 'AEIOU'  #  String  of  vowels
a = {}  #  Empty  dictionary
for  v  in  vowels:  #   v  is  each  vowel  of  string  vowels
    ctr = s . count(v)  #  Number  of  times  'v'  is  in  string
    if  ctr  > 0:
        a[v] = ctr  #  Appends  v :  ctr  to  dict  'a'  when  ctr > 0
print(a)

# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b.update(a)
print(b) # {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a.update(b)# Error beacuse a is list object

#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a) # Error
print(b) # {}
c = [(10,) , (20,) , (30,)]
b.update(c) # Error
print(b) # {}

#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) # {0:0,1:1,2:8,3:27,4:64}
print(type(d)) # <class 'dict'>

# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5)}
print(d) # {0:0,1:2,2:4,3:6,4:8}

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in  a .items()   if    k % 2 != 0}
print(b) # {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # {10 : 'Rama', 18 : 'Rajesh', 12 : 'Rama Rao'}

# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')
'''output:
    Begin
    Hyd
    Sec
    Cyb
    <class 'NoneType'>
    End'''

# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30 
# End  of  the  function
x = f1()
print(x) #  (10, 20, 30)
print(type(x)) # <class 'tuple'>
a , b , c =  f1()
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop') # for  loop
for  k   in  f1():
	print(k) # 10 nextline 20 nextline 30
        
# Find  outputs
def f1():
    return  10
    return  20
    return  30
# End  of  the  function
print('Begin') # Begin
x = f1()
print(x) # 10
print('End') # Ennd
#return 100 # Error

#  Find  outputs
f1() # Error f1 function is not defined
def f1():
    print('Hello')
print(f1()) # Hello
print(f1) # None

# Find  outputs  (Home  work)
print('Hello') # Hello is printed First
def  f1():
    print('f1  function')
#End  of   function
print('Hi') # Hi is printed Second 
print(f1()) #  f1 Function is printed and None
print(f1) # <function f1 at 0x79ba4634c180>
print('Bye') # Bye is last printed

#  Find  outputs
def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')
#End  of  the  function
print('Begin') # Begin 
print(type(f1)) # <class 'function'>
print(id(f1)) # address of function a
print('End') # End

#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20)) # 30
print(add('Hyder' , 'abad')) # Hyderabad
print(add(10.8 , 20.6)) # 31.40
print(add(True , False)) # 1
print(add(3 + 4j , 5 + 6j)) # (8+10j)
print(add(25 , 10.8)) # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) #[25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10,'20')) # not possible int and str are not added
          
# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Three  argument  function : 10,20,30
f1(40 ,50) #  Error 
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
	for   i    in   range(2 , n // 2 + 1):  #  Range  of  divisions  is  2  to  n // 2
		if  n % i == 0: # Is  'i'  a  divisor  of  'n'
			return  False #  'n'  is  not  prime
	#  End  of  for  loop
	return  True  #  'n'  is  prime
'''
1) prime(25)  --->  False
    How  many  times  is  for  loop  executed ?  --->  4  times

2) prime(11) --->  True
    How  many  times  is  for  loop  executed ?  --->  4  times

3) prime(2) ---> True
    How  many  times  is  for  loop  executed ?  ---> 0  times

4) prime(49) --->  False
    How  many  times  is  for  loop  executed ?  --->  6  times

5) range(2 , n / 2 + 1)
    What  is  the  issue  with the  statement ?  --->  /  is  a  float  operator  but  range()  can  not  have  float  operands

6) for  i  in  range(2 , n // 2 + 1):
	    if  n % i == 0:
			return   False
	   else:
   	        return  True
    What are  the  two  issues  with  else ?  --->  for  loop  is  executed  only  once  and prime(25)  returns  True  even  though  25  is  not  a  prime  number

7) for  i  in  range(1 , n // 2 + 1):
	    if  n % i == 0:
			return   False
     What  is  the  issue  with  the  above  for  loop ? ---> Every  number  is  divisible  with  1  and  hence  start  from  2

8) for  i  in  range(2 , n):
	    if  n % i == 0:
			return   False
    What  is  the  issue  with  the  above  for  loop ? ---> There  are  no  divisors  beyond  n //  2  and  hence  don't  proceed  upto  n - 1
'''
n = int(input('Enter  any  integer  number  :  '))
if  n < 2:  #  1  is  neither  prime  not  composite
	print('Invalid  input')
elif  prime(n):  #  Is  'n'  prime  number
	print('Prime  number')
else:
	print('Composite  number')

# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)
'''  output:
Emp Number  :  25 Emp Name : Rama  Rao 	 Salary  :  10000.0
Emp  Number  :  Sita Emp Name  :  20000.0 	  Salary  :  35'''