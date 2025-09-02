'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor changes
Enter String:RamA raO
{'A': 3, 'O': 1}
'''
a = input("Enter any string:").upper()
print(a)
vowels = ['A', 'E', 'I', 'O', 'U']
b = {}
count = 0
for i in a:
    if i in vowels:
        b[i] = a.count(i)
print(b)

'''
Outputs:

Enter any string:RamA raO
RAMA RAO
{'A': 3, 'O': 1}
'''








# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')] # Ref 'a' points to list of tuples
b = {'Y' : 'Yellow', 'G' : 'Gray'} # Ref 'b' points to dictionary of 2 key value pairs
b . update(a) # updates elements of tuples of list 'a' to dictionary 'b'
print(b) #  # prints {'Y' : 'Yellow', 'G' : 'Green', 'R' : 'Red', 'B' : 'Blue'}
a.update(b) # Error because 'a' is list and list has no update method









#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)] # Ref 'a' points to list of tuples
b = {} # Ref 'b' points to empty set
b.update(a) # Error because dictionary requires only 2 values but given 3 values
print(b) # prints empty dictionary i.e., {}
c = [(10,) , (20,) , (30,)] # Ref 'c' points to list of tuples
b . update(c) # Error because dictionary requires 2 values but given only 1 value
print(b) # prints empty dictionary i.e., {}









#  Find  outputs (Home  work)
d = {x : x ** 3 for x in range(5)} # dictionary comprehension
print(d) # prints 'd' {0 : 0, 1 : 1, 2 : 8, 3 : 27, 4 : 64}
print(type(d)) # prints type od 'd' i.e., <class 'dict'>









# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5)} # Ref 'd' points to dictionary comprehension
print(d) # prints 'd' i.e., {0 : 0, 1 : 2, 2 : 4, 3 : 6, 4 : 8}









# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'} # Ref 'a' points to dictionary of 5 key value pairs
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # prints 'd' i.e., {15 : 'Sita', 17 : 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # prints 'c'i.e., {10 : 'Rama', 18 : 'Rajesh, 12 : 'Rama Rao'}









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

'''
Outputs:

Begin
Hyd
Sec
Cyb
<class 'NoneType'>
End
'''









# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)
print(type(x))
a , b , c =  f1()
print(a)
print(b)
print(c)
print('for  loop')
for k in f1():
	print(k)


'''
Outputs:

(10, 20, 30)
<class 'tuple'>
10
20
30
for loop
10
20
30
'''









# Find  outputs
def    f1():
        return  10
        return  20 
        return  30
# End  of  the  function
print('Begin')
x = f1()
print(x)
print('End')
#return 100 # Error because return should be inside the function

'''
Outputs:

Begin
10
End
'''














#  Find  outputs
#f1() # Error function call should be after defining function
def   f1():
        print('Hello')
print(f1()) # prints Hello
print(f1) # prints None









# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

'''
Outputs:

Hello
Hi
f1 function
None
Bye
'''









#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')

'''
Outputs:

Begin
<class 'function'>
address of function f1
End
'''









#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20)) # prints 30
print(add('Hyder' , 'abad')) # prints 'Hyderabad'
print(add(10.8 , 20.6)) # prints 31.4
print(add(True , False)) # prints 1
print(add(3 + 4j , 5 + 6j)) # prints (8 + 10j)
print(add(25 , 10.8)) # prints 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) # [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10,'20')) # Error because int and string cannot be added
          








# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z) # if functions have same name then last function is executed
f1(10 , 20 , 30) # prints i.e., Three argument function: 10 20 30
f1(40, 50) # Error becuase we have given 2 arguments but required are 3 arguments
f1(60) # Error becuase we have given 1 argument but required are 3 arguments
f1() # Error becuase we have given 0 arguments but required are 3 arguments









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
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
if n > = 2:
    print("Invalid input")
elif prime(n):
    print("Prime number")
else:
    print("Composite number")

'''
1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  ---> 4 times

2) prime(11) --->
    How  many  times  is  for  loop  executed ?  ---> 10 times

3) prime(2) --->
    How  many  times  is  for  loop  executed ?  ---> 1 time

4) prime(49) --->
    How  many  times  is  for  loop  executed ?  ---> 48 times
'''










# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita', 20000.0, 35)

'''
Outputs:

Emp Number : 25<tab>Emp Name : Rama Rao<tab>Salary : 10000.0
Emp Number : Sita<tab>Emp Name : 20000.0<tabSalary : 35
'''
