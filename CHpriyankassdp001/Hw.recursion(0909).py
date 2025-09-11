#1 
"""Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 ,  1 ,  1 ,  2 , 3 ,  5 , 8 , ...

2) What  is  the  formula  for  10th  term ?  ---> 9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  ---> 0  and  1"""

def  fib(i):  #   'i'  is  term  number
    if  i==1:
        return  0
    if  i==2:
        return  1
    return  fib(i-1)+fib(i-2)


n = int(input('How many terms ? :  '))
print('Fibonacci  series')
print(fib(n))

#How  to  print  first  'n'  terms  of  fibonacci  series


"""def fib(i):  # 'i' is term number (1-based)
    if i == 1:  # 1st term
        return 0
    if i == 2:  # 2nd term
        return 1
    return fib(i - 1) + fib(i - 2)"""



#2


'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  ---> 1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  ---> 1
'''


def power(a , b):
    if  b>=1:
        return  a*power(a,b-1)
    if  b<0:
        return a*power(1/a,b+1)
    return  1

 #"""1) power(4.5 , 3) =

 #2) power(4.5 , -3) =

 #3) How  many  function  calls  are  in  power(a , b)  ? --->"""

a= float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(power(a,b))
# How  to  print  a , b  and  a ^ b


3

"""''
Write  a   recursive  function  to  reverse  a  number

rev(678) =  678 % 10 *  10 ^ (3 - 1)  +  rev(678 // 10)
              =  800  +  rev(67)
              =  800  +  67 % 10 * 10 ^ (2 - 1) + rev(67 // 10)
              =  800  +  70 + rev(6)
              =  800  +  70 + 6 % 10 * 10 ^ (1 - 1) + rev(6 // 10)
              =  800  +  70 + 6 + rev(0)
              =  800  +  70 + 6 + 0
     = 876

1) How  many  function  calls  are  in  rev(678) ?  --->   4

2) How  many  function  calls  are  in  rev(n-digit number)  ? ---> n + 1

3) How  to  obtain  length  of a  number ?  --->  len(str(n))
'''
from math import *
def  rev(n):
	if  ???
  return  ???
	else:
  return  ??
'''
rev(946)  =
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))"""


from math import *

def rev(n):
    if n == 0:  # if num is 0 then return 0
        return 0
    length = len(str(n))  # number of digits in n
    return (n % 10) * (10 ** (length - 1)) + rev(n // 10)

n = int(input("Enter any number: "))
print("Reverse Number:", rev(n))


4

#  Tricky  program
#   Find  outputs
def  f1():#define the function 
    global  a# it request the a consider as global variable 
    if  a:# a is non zero 
        print(a)#3. ,2,1
    a = a - 1#3-1=2 ,2-2=1,1-1=0
f1() #call the f1 function
print('Hello')
print('Hi')
print(a)
print('Bye')#bye
# End  of  the  function
a = 3#global variable 
f1()#function call
print('End')#End

#output
"""3
2
1
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
End"""



5

 #   Find  outputs
def  f1():#function header 
    a = 3#local variable 
    if  a: #a is true
        print(a)#3
    a = a - 1#3-1=2
f1()# again call the function 
print('Hello')
print('Hi')
print(a)
print('Bye')
#End  of  the  function
a = 3#Global variable 
f1()#function call
print('End')
# output
"""
3
3
3....
"""


6

#  Most  tricky   program
# Find  outputs  (Home  work)
def  f1(x , y):#function header
    if   x > 40:#if x>40
        return
        x+=y #x=x+y
    f1(x , y)#recursive function 
    print(x)#prints the x 
#End  of  the  function
x = 10#global variable 
f1(x , x := x + 1)#call the f1 function i.e.10,10+1=11
print(x)#11

"""#1st xis 10 y is 11 
10>40-false
10+11=21
#2nd x is 21 y is 11 
21>40-false
21+11=32
#3rd x is 32 y is 11 
32>40-false
32+11=43
#4th x is 43 y is 11 
43>40-true
Return immediately """
#output
"""43
32
21
11"""

7

 # Find  outputs   (Home  work)
def  f1(x):#define the f1 function
    print(x)#3
    if   x: #True non zero 
        f1(x - 1) #call the function f1(3-1)
        print(x)#2,1,0,0,1,2,3
# End  of  the  function
f1(3)#call the function 


8

 #  Find  outputs
def  f1():#define the f1 function 
	print('f1  function')#f1 function
	f2()#error
	print('End  of  f1  function')#end of f1 function
def  f2():
	print('f2  function')#f2 function
	f1()#error
	print('End  of  f2  function')#enf of f2 function 
f1()#function call


9

 #  Find  outputs  (Home  work)
def    f1():#function header f1()
        print('f1    function')#f1    function
def    f2():
        print('f2  function')#f2 function 
# End  of  the  function
f1()#call the f1()
f2()#call the f2()
print(f1  is  f2)#False
f2 = f1 #f2ref points to f1() function
f2()#call the function 
print(f1  is  f2)# True 
f2 = f1()#it returns nothing 
print(f2)#None
f2()#error 


10

# Find  outputs (Home  work)
p=print
#How  to  assign  ref  'p'  to  print()  function
print(p('Hyderabad'))
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello')
print(p('Hello'))
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'


11

 # Find   outputs (Home  work)
x=id
#How  to  assign  ref  'x'  to  id()  function
print(x())
#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p=len
#How  to  assign  ref  'p'  to  len()  function
print(p('Hyd'))
#How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd


12

# Find  output(Home  work)
def    f1(a):#function header
    def   f2():#define nested function
        return  10#returns 10
	# End  of  f2  function
    return  f2() + 20 +  a #here call the f2 function and also returna the results of of this expression i.e.10+20+30=60
# End  of  f1  function
print(f1(30))#call the function i.e.60



13

 # Find  outputs (Home  work)
def  outer():
    print('Outer  function')#Outer function 
    def  inner1():#inner 1function header 
        print( '1st  inner  function')#1st inner function 
    def  inner2():
        print('2nd  inner  function')#2nd inner function 
    print('Hi')#Hi
    inner2()#call the inner2 function
    print('Hello')#Hello
    inner1()#call the inner 1 function
    print('Back  to  outer  function')#Back  to  outer  function
# End of the function
print('Begin')#Begin
outer()#call the outer function 
print('Bye')


14

 # Find  outputs  (Home  work)
x = 10#global variable 
def  outer():#define the outer function 
    x = 20 #local variable x=20
    def   inner():
        x = 30#local variable 
        print(x)#30
        print(globals()['x'])#10
    inner()#call the inner function 
outer()#call the outer function 
print('Bye')#Bye


16

# Find  outputs  (Home   work)
x = 10  #  Gv
def  outer():#function header
    x = 20#local variable 
    def   inner():#inner function header
        print(x)#20
    print(globals()['x'])#10
    inner()#call the inner function
outer()#call the outer function 


17

 # Find  outputs  (Home  work)
x = 10 #x is the global variable 
def  outer():#define the outer function 
    def   inner():#define the inner function 
        print(x)#10 due to x is global variable 
    inner()#calls the inner function 
outer()#call the outer function 


18

# Find  outputs  (Home  work)
def  outer():#define the function 
    x = 10#local variable x=10
    def  inner(): #define the inner function 
        x = 20 #local variable 
        print(x)#20
        x +=  7#20+7=27 but no use
	# End  of  inner  function
    print(x)#10
    x += 5#10+5=15
    inner()#call the inner function 
    print(x)#15
# End  of  the  function
outer()#call the outer function 
print('Bye')#Bye