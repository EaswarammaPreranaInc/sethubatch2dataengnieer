

'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
s=input("Enter String: ")
m={}
vowels='AEIOU'
for x in s.upper():
    if x in vowels :
        if x in m:
            m[x]+=1
        else:
            m[x]=1
print(m)
        





# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b) # {'Y':'Yellow','G':'Green','R':'Red','B':'Blue'}
a . update(b) # Error



#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a) # error
print(b)
c = [(10,) , (20,) , (30,)]
b . update(c) # error
print(b)





#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) # <class 'dict'>



# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) # {0:0,1:2,2:4,3:6,4:8}



# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # {15:'Sita',17:'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # {10:'Rama',18:'Rajesh',12:'Rama Rao'}




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

output:   
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
	
Output:
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
return   100 # Error

'''OUTPUT:
Begin
10
End




#  Find  outputs
#f1() # Error
def   f1():
        print('Hello')
print(f1()) # None
print(f1) # <function f1 at hexadecimal>





# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

Output:
Hello
Hi
f1 function
None
<function f1 at hexadecimal>
Bye




#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20)) # 30
print(add('Hyder' , 'abad')) # Hyderabad
print(add(10.8 , 20.6)) # 31.4
print(add(True , False)) # 1
print(add(3 + 4j , 5 + 6j)) # 8+10j
print(add(25 , 10.8)) # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) # [25 , 10.8 , 'Hyd' , True , None , 3+4j , 'Sec']
print(add(10 , '20')) # error





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
f1(40 , 50) # two argument function : 40 50
f1(60) # one argument function : 60
f1() # No-argument function




def   prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
        else:
            continue
    return True
n=int(input("Enter a number: "))
if   not prime(n) or n==4:
	print('Invalid  input')
elif  prime(n):
	print('Prime  number')
else:
	print('Composite  number')




# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) # Emp  Number : Rama  Rao     Emp Name  :  Rama  Rao    Salary  :  10000.0
disp('Sita' , 20000.0 , 35) # Emp  Number  :  Sita     Emp Name  :  20000.0     Salary  :  35
