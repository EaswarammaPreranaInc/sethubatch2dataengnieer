'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes

Sample output:
Enter String:RamA raO
{'A': 3, 'O': 1}
'''

#Program:
a = input("Enter mixed case string: ")
a = a.upper()
vowels = set("AEIOU")
found = vowels.intersection(a)
d = dict()
for v in found:
    d[v] = a.count(v)
print(dict(sorted(d.items())))





# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)				# {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a . update(b)				# Error





#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)				# Error
print(b)				# {}
c = [(10,) , (20,) , (30,)]
b . update(c)				# Error
print(b)				# {}





#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)			# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))			# class 'dict'>





# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)			# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}





# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)										# {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)										# {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}





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

#Output:
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End




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
for  k   in   f1():
	print(k)

#Output:
(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30




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
return   100

#Output:
Begin
10
End




#  Find  outputs
f1()				# Error
def   f1():
        print('Hello')
print(f1())
print(f1)

#Output:
Hello
None
<function f1 at 0x0000022416E78A40>




# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

#Output:
Hello
Hi
f1  function
None
<function f1 at 0x0000017849918A40>
Bye




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

#Output:
Begin
<class 'function'>
1528025745984
End




#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))							# 30
print(add('Hyder' , 'abad'))						# Hyderabad
print(add(10.8 , 20.6))							# 31.4
print(add(True , False))						# 1
print(add(3 + 4j , 5 + 6j))						# 8+10j
print(add(25 , 10.8))							# 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))		# [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))							# Error





# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)						# Three  argument  function :  10 20 30
f1(40 , 50)							# Error
f1(60)								# Error
f1()								# Error





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
'''
How  to  read  a  number
if   input  is  invalid:
	print('Invalid  input')
elif  input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')
'''

#Program:
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
num=int(input("Enter a number: "))
prime(num)
if prime(num):
    print('Prime number')
else:
    print('Not a Prime')




# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)

#Output:
Emp  Number  :  25 <tabspace> Emp Name  :  Rama  Rao <tabspace> Salary  :  10000.0
Emp  Number  :  Sita <tabspace> Emp Name  :  20000.0 <tabspace> Salary  :  35