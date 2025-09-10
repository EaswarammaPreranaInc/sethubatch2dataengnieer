'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

s=input().upper()
l=sorted(s)
a={}
for ch in s:
    if ch in "AEIOU":                 # check if it's a vowel
        a[ch] = a.get(ch, 0) + 1
print(a)


# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) # appends all the elements of inner tuple to b
print(b) {'Y' : 'Yellow', 'G' : 'Green' , 'R': 'Red', 'B' : 'Blue'}
a . update(b)# error because there is no update method for list class

#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a) # error as nested sequence should have exactly 2 elements only
print(b) # empty dict
c = [(10,) , (20,) , (30,)]
b . update(c) # error as nested sequence should have exactly 2 elements only
print(b) # empty dict

#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)	# { 0:0,1:1,2:8,3:27,4:64}
print(type(d))	# class dict

# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) # { 0:1,1:2,2:4,3:8,4:16}

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)  # { 15:'sita', 17:'kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # {10 : 'Rama' , 18 : 'Rajesh' , 12 : 'Rama Rao'}

# Find outputs  (Home  work)
def   f1():			# 3.the statements of the function are executed
	print('Hyd')		# Hyd
	print('Sec')		# Sec
	print('Cyb')		# Cyb
# End  of  the  function
print('Begin')	# 1.execution starts from this statement 
x = f1()	# 2.the function is called so execution goes to function
print(x)	# 4.prints none as nothing is returned from the function
print(type(x)) 	# 5.class nonetype
print('End')	# 6.prints end

# Find  outputs  (Home  work)
def  f1():		# 2
	return  10 , 20 , 30	# return a tuple of 3 elements
# End  of  the  function
x = f1() 	# 1. function call 
print(x)	#3. (1,20,30)
print(type(x))	
a , b , c =  f1() 	# unpacks tuple to individual elements
print(a)	# 10
print(b)	# 20
print(c)	# 30
print('for  loop')
for  k   in   f1():
	print(k)		# iterates through the 3 elements of tuple

# Find  outputs
def    f1():			# 3
        return  10		# only one return should be there
        return  20		# the statements after return are skipped
        return  30
# End  of  the  function
print('Begin')		# 1. prints begin
x = f1()		# 2. function call
print(x)		# 4. prints 10
print('End')		# 5. prints end
return   100		# error as return statement should be in function 

#  Find  outputs
f1()			# function call should be there after the definition of the function so error
def   f1():
        print('Hello')
print(f1())		# function is not defined
print(f1)		# no object f1 in the current prgm
return   100		# error as return statement should be in function 

#  Find  outputs
f1()		# function call should be there after the definition of the function so error
def   f1():
        print('Hello')
print(f1())		# function is not defined
print(f1)		# no object f1 in the current prgm

# Find  outputs  (Home  work)
print('Hello')		# 1. prints hello
def  f1():		# 4. executes the statements in fucntion
        print('f1  function') # prints f1 function
#End  of   function
print('Hi')		# 2.prints hi
print(f1())		# 3. function call goes to function and prints none as f1 function is returning nothing
print(f1)		# 5. prints the function name address of f1 function
print('Bye')		# 6. prints bye

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')			# 1. prints begin	
print(type(f1))			# 2. class funtion
print(id(f1))			# 3. prints the address of function
print('End')			# 4. prints end

#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))		# prints 30
print(add('Hyder' , 'abad'))	# prints Hyderabad
print(add(10.8 , 20.6))		# prints 31.4
print(add(True , False))	# prints 1
print(add(3 + 4j , 5 + 6j))	# prints 8+10j
print(add(25 , 10.8))		# prints 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))	# concatenates the lists [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))	# erro as we cant add int to string

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)       # all the above functions are discarded as the last function is defined with same name
f1(10 , 20 , 30) # this will call the last function  Three  argument  function :  10 20 30
f1(40 , 50)    # this will give error as last function has 3 arg but call has 2 arguments
f1(60)      # this will give error as  as last function has 3 arg but call has 1 arguments
f1()   # this will give error as  as last function has 3 arg but call has 0 arguments

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

def   prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2):  
        if n % i == 0:
            return False
    return True
    if n.isdigit==False:
        return 'invalid'
try:
    n=int(input())
except:
    print('invalid input')
    exit()
if(prime(n)):
    print('Prime number') 
else:
    print('Composite number')


# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)    # Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0
disp('Sita' , 20000.0 , 35)   # Emp  Number  :  Sita      Emp Name  :  20000.0          Salary  :  35

