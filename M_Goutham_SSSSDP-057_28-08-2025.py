'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
'''
Enter String:RamA raO
{'A': 3, 'O': 1}
'''
n = input("Enter String: ").upper()
vowles = 'AEIOU'
d = {i : n.count(i) for i in n if i in vowles}
print(d)

                    #or

n = input("Enter the string: ")
vowels = 'AEIOU'
d = {}
for i in n:
    if i in vowels:
        d[i] = n.count(i)
print(d)

'''Enter String: rAma rao
{'A': 3, 'O': 1}'''




# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')] #Reference a points to list of tuples
b = {'Y' : 'Yellow', 'G' : 'Gray'} #Reference b points to dict obj 
b . update(a) #Here dict a is concatinated to dict b #all the key-value pairs of dict a is added to dict b
print(b) #{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a . update(b) #Error #a is a list where update() is not their in list class




#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)] #Reference a points to list of tuples
b = {} #Reference b points to empty dict
b.update(a) #Error as inner sequence should only contain exactly two elements
print(b) #Returns the empty dict i.e {}
c = [(10,) , (20,) , (30,)] #Reference c points to list of tuples 
b . update(c) #Error as inner sequence should contain exactly 2 elements but here we have only 1 element
print(b) #Returns the empty dict 



#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)} #Dict comphrension where each iteration x will be key and x**3 is the value
print(d) #Returns the key value pairs i.e {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) #<class 'dict'>



# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) } #Here dict comprehension where each iteration x will be key and 2*x will be the value
print(d) #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}



# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'} #Reference a points to dict obj
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0} #Here dict comprehension where each iteration k will be the key and value will be v and here is a condition where k % 2 != 0
print(b) #{15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')} #Here the condition will be the value must starts with R
print(c) #{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}



# Find outputs  (Home  work)
def   f1(): #It is the function header
	print('Hyd') #Stmt 1 
	print('Sec') #Stmt 2
	print('Cyb') #Stmt 3
# End  of  the  function #Default return for function is None
print('Begin') #Prints the begin #1st output
x = f1() #Here Reference x points to a function call 
print(x) #Returns the function call i.e executes the all statements in the function
print(type(x)) #<class 'NoneType'> #Because what function returns that will be the type of function
print('End') #Prinst the end #last output




# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30 #Here a function is defined with name f1 and returning a tuple i.e 10,20,30
# End  of  the  function
x = f1() #Here reference x points to a function call
print(x) #Returns the tuple i.e (10,20,30)
print(type(x)) #Returns the type i.e <class 'tuple'>
a , b , c =  f1() #Here a,b,c points to a function call 
print(a) #10
print(b) #20
print(c) #30
print('for  loop') #Returns the string 'for loop'
for  k   in   f1(): #Here we are calling the function with for loop i.e 
	print(k) 
#10
#20
#30
	


# Find  outputs
def    f1(): 
        return  10
        return  20 #For When ever the return statement in the function is their the function returns the return value and rest of the code will be skipped
        return  30
# End  of  the  function
print('Begin') #prints the Begin
x = f1() #Reference x points to the function call
print(x) #prints the return value of the function i.e 10
print('End') #Returns the End
#return   100 #Error #Return statement should be inside a function



# f1()   # Error because function must be defined before calling
def f1():
    print('Hello')

print(f1())  # Prints "Hello" and then prints None (since f1 has no return statement)
print(f1)    # Prints the function object reference (memory address of f1)




# Find  outputs  (Home  work)
print('Hello') #Prints the Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') #Prints the 'Hi'
print(f1()) #Prints the 'f1 function' and returns the None
print(f1) #Returns the function object reference (memeory address of f1)
print('Bye') #Prints 'Bye'




#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') #Prints the 'Begin'
print(type(f1)) #Returns the type i.e <class 'function'>
print(id(f1)) #Returns the address of f1 
print('End') #Prints the 'End'




#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20)) #Returns the 10 + 20 i.e 30
print(add('Hyder' , 'abad')) #Concatinates the both strings and returns the string i.e 'Hyderabad'
print(add(10.8 , 20.6)) #Returns the addition of 10.8 + 20.6 i.e 31.4
print(add(True , False)) #Returns the 1 + 0 i.e 1
print(add(3 + 4j , 5 + 6j)) #Returns the addition of two complex numbers i.e (8+10j)
print(add(25 , 10.8)) #Returns the addition of int and float i.e 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) #Returns the list with elements of both lists i.e [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20')) #Error #We cannot concatinate int and string obj




# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) #Here it calls the 3 argument function i.e Three  argument  function :  10 20 30
f1(40 , 50) #Error #because all the functions are created with same name f1 and last function is considered and when we call fucntion with 3 arguments then it is called or else error
f1(60) #same problem here also
f1() #same problem



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
	
def prime(n):
    if n < 2:
          return False
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

'''output:
Enter a number: 11
Prime number
'''
	
	
# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) #Here the output will be i.e #Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0
disp('Sita' , 20000.0 , 35)#Here the output will be i.e #Emp  Number  :  Sita      Emp Name  :  20000.0    Salary  :  35


