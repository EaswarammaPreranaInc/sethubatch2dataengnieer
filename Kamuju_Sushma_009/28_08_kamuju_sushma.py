#1
'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
s=input("Enter the string: ")
s=s.upper()
s1={'A','E','I','O','U'}
s=sorted(s)
d={}
for x in s:
    if x in s1:
        d[x]=d.get(x,0)+1
print(d)



#2
# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) # 'a' is not dictionary to append the k-v pairs to b 
print(b) #{'Y' : 'Yellow', 'G' : 'Gray'}
a . update(b) #error, list cannot hold k-v pairs

#3
#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a) ## 'a' is not dictionary to append the k-v pairs to b 
print(b) #{}
c = [(10,) , (20,) , (30,)]
b . update(c) # 'c' is not dictionary to append the k-v pairs to b 
print(b) #{}

#4
# #  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) #{1:1,2:8,3:27,4:64}
print(type(d)) #<class 'dict'>

#5
# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) #{1:2,2:4,3:6,4:8}

#6
# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) #{ 15 : 'Sita' ,17 : 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) #{10 : 'Rama' ,18 : 'Rajesh' ,12 : 'Rama Rao'}

#7
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
#Begin
#Hyd
#Sec
#Cyb
# None 
# <class 'None'>
# End 

#8
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1() 
print(x) #(10,20,30)
print(type(x)) #<class 'tuple'>
a , b , c =  f1()
print(a) #10
print(b) #20
print(c) #30
print('for  loop')
for  k   in   f1():
	print(k) #10 20 30 
	
#9
# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin') #Begin
x = f1() 
print(x) #10
print('End') #End
# return   100 #cannot use return outside function

#10
#  Find  outputs
f1() #cannot call function before defining it 
def   f1():
        print('Hello')
print(f1()) 
# print(f1) #error, this is not the way to call function 
#output:
# Hello
# None


#11
# Find  outputs  (Home  work)
print('Hello') 
def  f1():
        print('f1  function') 
#End  of   function
print('Hi')
print(f1())
print(f1) #error
print('Bye')

#output
# Hello
# Hi
# f1 function
# None 
# Bye 


#12
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
#output:
# Begin
# <class 'function'>
# address of function object 
# End
#13
#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20)) #30
print(add('Hyder' , 'abad')) #Hyderabad
print(add(10.8 , 20.6)) #31.4
print(add(True , False)) #1
print(add(3 + 4j , 5 + 6j))#(8+10j)
print(add(25 , 10.8)) #35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) #error, list and string cannot be concatinated and we should pass only 2 arguments
print(add(10 , '20')) #error, seq and non seq cannot be concatinated with '+'

#14
# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) #Three  argument  function :  10 20 30
f1(40 , 50) #Two  argument  function : 40 50
f1(60) #Single  argument  function  : 60
f1() #No-argument  function

#15
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
def   prime(n):
	# return  true   when  'n'  is  prime  number  and  False  otherwise
	for i in range(2,n/2+1):
		if n%i==0:
			return False
	return True
try:
    n=int(input("Enter number: "))
    if(prime(n)):
        print("Prime Number")
    else:
        print("Composite Number")
except:
	print("Invalid Input")
# How  to  read  a  number
# if   input  is  invalid:
# 	print('Invalid  input')
# elif  input  is  prime  number:
# 	print('Prime  number')
# else:
# 	print('Composite  number')
	
#16
# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) #Emp  Number  :  25      Emp Name  :  Rama Rao       Salary  :  10000.0
disp('Sita' , 20000.0 , 35) #Emp  Number  :  Sita      Emp Name  :  20000.0       Salary  :  35
