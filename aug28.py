1.

(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes


s=input('enter string:')
s=s.upper()
vowels='AEIOU'
a={}
for v in vowels:
	ctr=s.count(v)
	if ctr>0:
		a[v]=ctr
print(a)
#output  : dhanush
{'A':1, 'U':1}}





2.

Enter String:RamA raO
{'A': 3, 'O': 1}


#output is {'A':3, 'O':1}




3.
# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)    
print(b)   #{'Y' : 'Yellow', 'G' : 'Green', 'R' : 'Red', 'B' : 'Blue'}
a . update(b)  #error, lists don't have update




4.

#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}   #empty dictionary
b.update(a)   #error, as dictionary neds key, value pairs
print(b)   # {}
c = [(10,) , (20,) , (30,)]
b . update(c)   #error as dictionary needs key value pairs but c has only list of tuples
print(b)   #{}



5.

#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)  #{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))  #<class 'dict'>


6.

# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)  #{0:0, 1:2, 2:4, 3:6, 4:8}


7.

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)  #{15:'Sita', 17:'rajesh'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)   #{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}


8.

# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')  #Begin
x = f1()     #Hyd<nxt line>Sec<nxt line>Cyb<nxt line>  
print(x)     #None
print(type(x))   #<class 'function'>
print('End')  #End  



9.

# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()   #(10,20,30)
print(x)   #(10,20,30)
print(type(x))  #<class 'tuple'>
a , b , c =  f1()   #a,b,c = (10,20,30)
print(a)  #10
print(b)  #20
print(c)  #30
print('for  loop')   #for loop
for  k   in   f1():
	print(k)   #10<nxt line>20<nxt line>30<nxt line> 


10.

# Find  outputs
def    f1():
        return  10  #As soon as Python hits the first return, the function immediately exits.
        return  20  #ignored
        return  30  #ignored
# End  of  the  function
print('Begin')  #Begin
x = f1()   #10
print(x)   #10
print('End')   #End
return   100   #error, return cannot be outside function



11.

#  Find  outputs
f1()     #error, f1() is not defined but called, hence error
def   f1():
        print('Hello')
print(f1())   #Hello<next line> None
print(f1)    #<function f1 at 0x0000021AB7A3D700>



12.

# Find  outputs  (Home  work)
print('Hello')   #Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')  #Hi
f1()
print(f1())  #f1 function<nextline>None
print(f1)   #<function f1 at 0x0000021AB7A3D700>
print('Bye')  #Bye


13.

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')  #Begin
print(type(f1))   #<class 'function'>
print(id(f1))   #140574829123456 
print('End')   #End



14.

#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))   #30
print(add('Hyder' , 'abad'))  #Hyderabad
print(add(10.8 , 20.6))  #31.4
print(add(True , False))   #1
print(add(3 + 4j , 5 + 6j))  #8+10j
print(add(25 , 10.8))   #35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))  #[25 , 10.8 , 'Hyd', True , None , 3+4j , 'Sec']
print(add(10 , '20'))   #error: as int 10 and string 20 is not possible to add



15.

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)  #'Three  argument  function : 10 , 20 , 30
f1(40 , 50)   #error
f1(60)    #error
f1()   #error


16.

# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)   #Emp  Number  :  25 	  Emp Name  :  Rama  Rao 	  Salary  :  10000.0
disp('Sita',20000.0,35)   #Emp  Number  :  Sita 	  Emp Name  :  20000.0 	  Salary  :  35

 