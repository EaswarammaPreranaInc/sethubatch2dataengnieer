''' 1) Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)
Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}
Hint:  Same  as  prog23a  with  minor  changes
'''

n = input("Enter the string: ").upper()
vowels = 'AEIOU'
d = {}
for i in n:
    if i in vowels:
        d[i] = d.get(i, 0) + 1
print(d)

'''
# Output:
Enter String: rAma rao
{'A': 3, 'O': 1}
'''



# 2) Find outputs (Home  work)

a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')] #Reference a points to list of tuples
b = {'Y' : 'Yellow', 'G' : 'Gray'} #Reference b points to dict obj 
b . update(a) #Here dict a is concatinated to dict b #all the key-value pairs of dict a is added to dict b
print(b) # Output: {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a . update(b)  # Error as list class has no update method



# 3) Find  outputs  (Home  work)

a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)] #Reference a points to list of tuples
b = {} #Reference b points to empty dict
b.update(a) #Error as inner sequence should only contain exactly two elements
print(b) #Returns the empty dict i.e {}
c = [(10,) , (20,) , (30,)] #Reference c points to list of tuples 
b . update(c) #Error as inner sequence should contain exactly 2 elements but here we have only 1 element
print(b) #Returns the empty dict 



# 4) Find  outputs (Home  work)

d = {x : x ** 3   for    x   in  range(5)} 
print(d) # Output: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) # Output: <class 'dict'>



# 5) Find outputs   (Home  work)

d = { x :  2 * x    for    x   in   range(5) } 
print(d) # Output: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}



# 6) Find outputs  (Home  work)

a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'} 
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0} 
print(b) # Output: {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')} #Here the condition will be the value must starts with R
print(c) # Output: {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}



# 7) Find outputs  (Home  work)

def   f1(): #It is the function header
	print('Hyd') #Stmt 1 
	print('Sec') #Stmt 2
	print('Cyb') #Stmt 3
# End  of  the  function #Default return for function is None
print('Begin') #Prints the begin #1st output
x = f1() #Here Reference x points to a function call executes the all statements in the function
print(x) #Returns the function call i.e None
print(type(x)) #<class 'NoneType'> #Because what function returns that will be the type of function
print('End') #Prinst the end #last output
'''
# Output: 
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End
'''



# 8) Find  outputs  (Home  work)

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
for  k   in   f1():
	print(k)
'''
# Output: 
(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30
'''	



# 9) Find  outputs

def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
x = f1()
print(x)
print('End')
return   100 # Error as return is outside the function 
'''
# Output: 
Begin
10
End
'''



# 10) Find  outputs

f1()
def   f1():
        print('Hello')
print(f1()) 
print(f1) 
'''
# Output: 
Hello
None
<function f1 at 0x0000020230E5EFC0>
'''



# 11) Find  outputs  (Home  work)

print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
'''
# Output: 
Hello
Hi
f1  function
None
<function f1 at 0x0000020230C61440>
Bye
'''



# 12) Find  outputs

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
# Output: 
Begin
<class 'function'>
2208433565632
End
'''


# 13) Find  outputs (Home  work)

def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20)) # Output: 30 
print(add('Hyder' , 'abad')) # Output: Hyderabad
print(add(10.8 , 20.6)) # Output: 31.400000000000002
print(add(True , False)) # Output: 1
print(add(3 + 4j , 5 + 6j)) # Output: (8+10j)
print(add(25 , 10.8)) # Output: 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) # Output: [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20')) # Error as we cannot add int and str



# 14) Find  outputs (Home  work)

def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Output: Three  argument  function :  10 20 30
f1(40 , 50) # Error as 1 arg is missing because f1 has 3 arguments
f1(60) # Error as 2 arg are missing because f1 has 3 arguments
f1() # Error as 3 arg are missing because f1 has 3 arguments





''' 15) Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  ---> A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? ---> i =   2 , 3 , 4 , 5 , 6 , .....  12

3) Let  input   be  11
    What  is   the  range  of  divisors ? ---> i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  --->  return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop

How  to  read  a  number
if   input  is  invalid:
	print('Invalid  input')
elif  input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')
'''
	
def prime(n):
    for i in range(2, (n//2) + 1): 
        if n % i == 0: 
            return False
    return True

n = int(input("Enter a number: "))
if n < 2:
    print("Invalid input")
elif prime(n):
    print("Prime number")
else:
    print("Composite number")

'''
# Output: 
Enter a number: 11
Prime number
Enter a number: 25
Composite number
'''
	
	

# 16) Find  outputs  (Home  work)

def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)

'''
# Output:
Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0
Emp  Number  :  Sita      Emp Name  :  20000.0    Salary  :  35
'''

