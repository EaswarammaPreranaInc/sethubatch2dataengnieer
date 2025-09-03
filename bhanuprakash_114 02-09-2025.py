#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
f1(t = (10 , 20 , 30))

'''
(10,20,15,18)
<class 'tuple'>
4
'''(10, 20, 15, 18)
<class 'tuple'>
4#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18))
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))

def avg(*a):
    return sum(a) / len(a) if a else 0  # One-line average calculation

# Test cases
print(avg(10, 20, 15, 18))                      # Output: 15.75
print(avg(25, 10.8, True))                      # Output: (25 + 10.8 + 1) / 3 = 12.933...
print(avg(10.8, 20.6, 15.2, 14.9, 9.8))         # Output: 14.26
print(avg())                                    #  0
print(avg(25))                                  # 25.0
print(avg(3 + 4j, 5 + 6j))                      #  (4+5j)
tpl = (10, 20, 15, 18)
print(avg(*tpl))                                # Unpacked tuple, Output: 15.75
#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  functiona  :  (10, 20, 30)   	   b  :  40
f1(10 , 20 , 30 , b = 40)
f1(50 , b = 60)
f1(b = 70)
f1(b = 10 , a = (20 , 30 , 40))
f1(b = 10 , (20 , 30 , 40))
f1()
f1(10 , 20 , 30 , (10 , 20 , 30))
f1(10 , 20 , 30 , 40)
f1(25)
f1(10 , 20 , 30 , b = (10 , 20 , 30))
([10, 20], {30, 40}, (50, 60))       # Full tuple with all arguments
<class 'tuple'>                      # The type of 'a'

[10, 20]                             # First element
<class 'list'>                       # Type of first element

{30, 40}                             # Second element (set)
<class 'set'>                        # Type of second element

(50, 60)                             # Third element
<class 'tuple'>                      # Type of third element
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
'''
Write  a  program  to  print  mathematical  table  of  a  number

Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                       						 7 * 2 = 14
			  								 7 * 3 = 21
												 .....
											 7 * 10 = 70
'''
'''num = int(input("Enter table number: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

'''
Write a  program to print following pyramid
Input: 5

             A
            A B
           A B C
          A B C D
         A B C D E


	   i         ch
---------------------
       1         'A'

	   2         'A'  to  'B'

	   3         'A'  to  'C'

	   4         'A'  to  'D'

	   5         'A'  to  'E'n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # Print spaces
    print(' ' * (n - i), end='')

    # Print characters from 'A' up to (A + i - 1)
    for j in range(i):
        print(chr(ord('A') + j), end=' ')
    
    print()  # Move to next line
#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')
a : 10
b : 20
c : 30

a : 11
b : 40
c : 31

a : 50
b : 22
c : 32
Bye

'''
