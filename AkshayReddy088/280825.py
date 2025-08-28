'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes

Enter String:RamA raO
{'A': 3, 'O': 1}
'''

x1 = input("Enter a string:")
b = {}
x1 = sorted(set(x1.upper()))
x2 = set('AEIOU')
for x in x1:
    if x in x2:
        b[x] = b.get(x,0)+1
print(b)





# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)  # 'Y' : 'Yellow', 'G' : 'Green','R':'Red' 'B' : 'Blue'}
print(b)
a . update(b) # error


#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)  # error
print(b)
c = [(10,) , (20,) , (30,)]
b . update(c) # error
print(b) 


#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) # {0:0,1:1,2:8,3:27,4:64}
print(type(d)) # <class dict>

    
    
    # Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) # {0:0,1:2,2:4,3:6,4:8}

    
    
# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # {15:'Sita',17:'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # {10:'Rama',18:'Rajesh', 12:'Rama Rao'}




    
# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') # Begin
x = f1()
print(x) 
# Hyd
# Sec
# Cyb
# None
print(type(x)) # <class 'NoneType'>
print('End') # 'End'

    
    
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x) # 10,20,30
print(type(x)) # <class 'tuple'>
a , b , c =  f1()
print(a) # 10
print(b) # 20 
print(c) # 30
print('for  loop') # for loop
for  k   in   f1():
	print(k)
 #10
 #20
 #30

    
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
return 100   # Error

    
#  Find  outputs
f1()
def   f1():
        print('Hello')
print(f1()) 
# Hello
# None
print(f1) # Error



# Find  outputs  (Home  work)
print('Hello') # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # Hi
print(f1()) 
# Hello
# None
print(f1) # Error
print('Bye') # Bye



#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # Begin
print(type(f1)) # <class 'function'>
print(id(f1)) # some number
print('End') # End




#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20)) # 30
print(add('Hyder' , 'abad')) # Hyderabad
print(add(10.8 , 20.6)) # 31.4
print(add(True , False)) # 1
print(add(3 + 4j , 5 + 6j)) # (8+10j) 
print(add(25 , 10.8)) # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) # [25,10.8,'Hyd',True,None,3+4j,'Sec']
print(add(10 , '20')) # Error

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Three  argument  function :  10 20 30
f1(40 , 50) # Two argument function : 40,50
f1(60) # Single argument function : 60
f1() # No-argument function

    
    
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

def   prime(n):
	return  true   when  'n'  is  prime  number  and  False  otherwise

1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->

2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->

3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->

4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->

# How  to  read  a  number
if   input  is  invalid:
	print('Invalid  input')
elif  input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')
'''

try:
  y = int(input("Enter a number that you to check prime : "))
  def prime(x):
    if x > 1:
      for i in range(2,x):
        if x % i == 0:
          return False
      return True
except ValueError:
  print("Invalid Input, pls give interger")
else:
  if prime(y):
    print("Prime")
  elif(y > 1):
    print('Composite Number')
  else:
    print("Invalid Input , Input should be greater than 1")


    
    
# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) # Emp  Number  :  25 	  Emp Name  :  Rama  Rao 	  Salary  :  10000.0
disp('Sita' , 20000.0 , 35) # Emp  Number  :  Sita 	  Emp Name  :  20000.0 	  Salary  :  35