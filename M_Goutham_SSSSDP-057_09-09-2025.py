'''
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 ,  1 ,  1 ,  2 , 3 ,  5 , 8 , ...

2) What  is  the  formula  for  10th  term ?  ---> 9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  ---> 0  and  1
'''
def  fib(i):  #   'i'  is  term  number
	if i == 1 :
		return  0
	if i == 2:
		return 1
	return  fib(i-1) + fib(i-2)

#Using the function
n = int(input('How many terms ? :  '))
print('Fibonacci  series')
#How  to  print  first  'n'  terms  of  fibonacci  series
for i in range(1,n+1):
	print(fib(i),end=' ')

'''output:
How many terms ? :  5
Fibonacci  series
0 1 1 2 3
'''


'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  ---> 1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  ---> 1
'''
def  power(a , b):
	if  b == 0:
		return  1
	if  b < 0:
		return  (1/b)*power(a,b+1)
	return  a*power(a,b-1)
'''
1) power(4.5 , 3) =

2) power(4.5 , -3) =

3) How  many  function  calls  are  in  power(a , b)  ? --->
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
#How  to  print  a , b  and  a ^ b
print(f'{a} ^ {b} = {power(a,b)}')

'''output:
Enter  base :  4.5
Enter  power :  3
4.5 ^ 3 = 91.125
'''


'''
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
	if n > 0:
		return n%10 * 10**(len(str(n))-1) + rev(n//10)
	else:
		return 0
'''
rev(946)  =
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))

'''output:
Enter  any  number :  456
Reverse   Number :   654
'''


#  Tricky  program
#   Find  outputs
def  f1():
	global  a #Here we are asking to treat a as GV
	if  a: #Here condition is checked weather a is non-empty or not
		print(a) #prints the value 3
		a = a - 1 #Here a is modified to a-1
		f1() #F1 function is called 
		print('Hello') #prints the 'Hello'
		print('Hi') #prints the 'Hi'
		print(a) #prints the value of a
	print('Bye') #Prints the 'Bye'
# End  of  the  function
a = 3 #Ref a is pointing to value 3 #a = 2
f1() #Here f1() is called
print('End') #Prints the End
'''output:
3
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
End
'''



#   Find  outputs
def  f1():
	a = 3 #Here LV a points to value 3 #a = 0
	if  a: #Here condition is checked weather a is 0 or non-empty
		print(a) #Prints the value of a 
		a = a - 1 #Here a is modified by decrementing a
		f1() #Here f1 is called (recursive)
		print('Hello') #Prints the Hello
		print('Hi') #Prints Hi
		print(a) #Prints the value of a
	print('Bye') #Prints the Bye
#End  of  the  function
a = 3 #Here GV a points to the value 3
f1() #Here function f1 is called
print('End') #Prints the End
'''Output:
3
3
3
3
3
3
3
...Utill stack becomes full
'''



#  Most  tricky   program
# Find  outputs  (Home  work)
def  f1(x , y): #Here function is defined f1 with 2 formal parameters #32 , 11
	if   x > 40: #Here condition is checked weather x is greater than 40 or not
		return #Here we are returning nothing
	x += y #Here we are adding y to x i.e x = x+y i.e 10+11 =21  32 43
	f1(x , y) #Here again f1 is called recursively 21,11
	print(x) #Prints the value of x
#End  of  the  function
x = 10 #Here Gv x points to value 10
f1(x , x := x + 1) #Here we are passing actual parameters i.e 10,11
print(x) #Prints the value of x
'''output:
43
32
21
11
'''



# Find  outputs   (Home  work)
def  f1(x):
	print(x) 
	if   x:
		f1(x - 1) #3 2 1 0
	print(x)
# End  of  the  function
f1(3) #Here f1 function is called
'''outputs:
3
2
1
0
0
1
2
3
'''


#  Find  outputs
def  f1(): #Here f1 function is defined
	print('f1  function') #Prints the f1 function
	f2() #Error #We cannot call f2 function as there is no f2 function 
	print('End  of  f1  function') #Prints the End of f1 function
def  f2(): #Here f2 function is defined
	print('f2  function') #Prints the f2 function 
	f1() #f1 function is called
	print('End  of  f2  function') #Prints the End of f2 function
f1() #Here f1 function is called
'''outputs:
f1 function 
Error
End of the f1 function'''



#  Find  outputs  (Home  work)
def    f1(): #Here f1 function is defined 
        print('f1    function') #Prints the f1 function
def    f2(): #Here f2 function is defined
        print('f2  function') #Prints the f2 function
# End  of  the  function
f1() #f1 function is called
f2() #f2 function is called
print(f1  is  f2) #False
f2 = f1 #Here ref f2 points to f1 function
f2() #f2 function is called
print(f1  is  f2) #True as both f1 and f2 are pointing to same function f1
f2 = f1() #Here ref f2 pointing to function call f1
print(f2) #prints the function name and memory location in hexa decimal format
f2() #Error  

'''outputs:
f1 function
f2 function
False
f1 function
True
f1 function
Error
'''



# Find  outputs (Home  work)
p = print 		#How  to  assign  ref  'p'  to  print()  function
p('Hyderabad') 	#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None 	#Here we ref print points to None
#print('Hello') 	#Error #as already print function is pointing to None
p('Hello')		#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'



# Find   outputs (Home  work)
x = id			#How  to  assign  ref  'x'  to  id()  function
print(x(25)) 	#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p = len 		#How  to  assign  ref  'p'  to  len()  function
print(p('Hyd')) #How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd'




# Find  output(Home  work)
def    f1(a): #f1 function is defined with argument a
	def   f2(): #Inside f1 function f2 function is defined
		return  10 #F2 function is returning 10
	# End  of  f2  function
	return  f2() + 20 +  a #F1 function is returining f2 function + 20 + a
# End  of  f1  function
print(f1(30)) #f1 function is called and printed
'''outputs:
10 + 20 + 30 = 60
60 is returned
'''



# Find  outputs (Home  work)
def  outer(): #Here outer function is defined
	print('Outer  function') #Prints the Outer function
	def  inner1(): #Here inside outer function inner function is defined i.e inner1
		print( '1st  inner  function') #Print the 1st inner function
	def  inner2(): #Inside the outer function one more inner function is defined i.e inner2
		print('2nd  inner  function') #Prints the 2nd inner function
	print('Hi') #Prints the Hi
	inner2() #Inner2 is called
	print('Hello') #Prints the Hello
	inner1() #Inner1 is called 
	print('Back  to  outer  function') #Prints the Back to outer function
# End of the function
print('Begin') #Prints the Begin
outer() #Outer function is called
print('Bye') #Prints the Bye
'''
outputs:
Begin
Outer function
Hi
2nd inner function
Hello
1st inner function
Back to outer function
Bye
'''



# Find  outputs  (Home  work)
x = 10 #GV x points to value 10
def  outer(): #Outer function is defined 
	x = 20 #LV x points to value 20
	def   inner(): #Inner function is defined 
		x = 30 #LV of inner function x points to value 30
		print(x) #Prints the value of x i.e 30
		print(globals()['x']) #Here global variable x will be converted to key-value pair and prints its value i.e 10
	inner() #Inner function is called 
outer() #Outer function is called 
print('Bye') #Prints the 'Bye'
'''
outputs:
30
10
Bye
'''



# Find  outputs  (Home   work)
x = 10  #GV x points to value 10
def  outer(): #Outer function is defined 
	x = 20 #LV x points to value 20
	def   inner(): #Inner function is defined
		print(x) #Prints the value of x in the outer function i.e 20
		print(globals()['x']) #this function returns all the global variables into key-value pairs and here it returns the x value i.e 10
	inner() #Inner function is called i.e 20 
										 #10
outer() #Outer function is called i.e
'''
outputs:
20
10
'''



# Find  outputs  (Home  work)
x = 10 #Gv x points to value 10
def  outer(): #Outer function is defined 
	def   inner(): #Inner function is defined 
		print(x) #	Prints the value of x i.e 10
	inner()#inner function is called so prints value of x i.e 10
outer() #Outer function is called i.e 10

'''outputs:
10
'''



# Find  outputs  (Home  work)
def  outer():
	x = 10 #Here LV x points to value 10
	def  inner(): #Inner function is defined 
		x = 20 #Here inner LV x points to 20
		print(x) #Prints the 20
		x +=  7 #Here x is incremented by 7 i.e 27
	# End  of  inner  function
	print(x) #Prints the value of outer function x i.e 10
	x += 5 #outer x is incremented by 5 i.e 15
	inner() #inner function is called
	print(x) #X is printed i.e 15
# End  of  the  function
outer()
print('Bye')
'''
Outputs:
10
20
15
Bye

'''
