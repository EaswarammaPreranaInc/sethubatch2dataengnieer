# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)#{'Y' : 'Yellow', 'G' : 'Gray','R' :'Red' ,'G' : 'Green','B' : 'Blue}
a . update(b)#error


#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)
print(b)#{10 : 20 , 30 , 40 : 50 , 60,70 :80 , 90}
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b)#error

#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)#{1:1,2:8,3:27,4:64}
print(type(d))# <class set>

# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)#{1:2,2:4,3:6,4:8}

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)#{10:rama,18:'rajesh',12:'rama rao'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)#{10:rama,18:'rajesh',12: 'Rama Rao '


 # Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)#begin
Hyd
Sec
Cyb
End
print(type(x))#<class function>
print('End')

# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)#10
20
30
print(type(x))#<class function>
a , b , c =  f1()
print(a)#10
print(b)#20
print(c)#30
print('for  loop')
for  k   in   f1():
	print(k)#for loop
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
print(x)#30
End
print('End')
return   100#error

#  Find  outputs
f1()
def   f1():
        print('Hello')
print(f1())#hello
print(f1)#hello

# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
hello
hi
f1 function
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
#begin
Class function 
Adress of f1()
End

#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))#30
print(add('Hyder' , 'abad'))#Hyderabada
print(add(10.8 , 20.6))#30.14
print(add(True , False))#1
print(add(3 + 4j , 5 + 6j))#8+10j
print(add(25 , 10.8))#30.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))#error
print(add(10 , '20'))#error


# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
f1(40 , 50)
f1(60)
f1()
#Three  argument  function :  10 , 20, 30
#Two  argument  function :40,50
#Single  argument  function  :60
#No-argument  function
# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)
#Emp  Number  :  25            Emp Name  : Rama  Rao'
  Salary  : 10000.0)

'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''                                                                                                                                                             s=input("enter a string:")
s=s.upper()
b=sorted(s)
a={}
c="AEIOU"
for i in b:
   if i.isalpha():
       if i in c:
          a[i]=a.get(i,0)+1
print(a)                       enter aWrite   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  ---> A  number  without  divisors  except  1  and  itself
def prime(n):
   if n <= 1:
        return False
   for i in range(2, int(n**0.5) + 1):

        if n%i==0:
           return False
   return True
n=int(input("enter a number: "))
s=prime(n)
if s:
   print("It is a prime number")
else :
   print("It is a composite number")
      enter a number: 25
It is a composite number string:SraVani
{'A': 2, 'I': 1}