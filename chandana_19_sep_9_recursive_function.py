#   Find  outputs
def  f1():
	global  a # use global variable 'a'
	if  a:
		print(a)
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
a = 3
f1()
print('End')
'''
o/p:
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
End'''


#   Find  outputs
def  f1():
	a = 3
	if  a:
		print(a)
		a = a - 1
		#f1() # error : becomes a infinite loop as 'a' is a local variable inside the function, it resets to 3 every time.
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
#End  of  the  function
a = 3
f1()
print('End')
'''
o/p:
3
Hello
Hi
2
Bye
End
'''


# Find  outputs  
def  f1(x , y):
	if   x > 40:
		return
	x += y 
	f1(x , y)
	print(x)
#End  of  the  function
x = 10
f1(x , x := x + 1) # global 'x' is updated to 11 before function call
print(x)

'''
o/p:
43
32
21
11'''


# Find  outputs 
def  f1(x):
	print(x)
	if   x:
		f1(x - 1) # recursion call with x-1
	print(x) # print 'x' after recursion ends
# End  of  the  function
f1(3)
'''
0/p:
3
2
1
0
0
1
2
3
'''


'''
#  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1() # no if condition so it becomes an infinite loop by f1() calling f2() and f2() calling f1()
'''


#  Find  outputs 
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1() # f1 function
f2() # f2 function
print(f1  is  f2) # False : f1 and f2 are two different function objects
f2 = f1 # f2 refer to same function as f1
f2() # f1 function
print(f1  is  f2) # True : f1 and f2 refer to same function object
f2 = f1() 
print(f2) # f1 function and f1() has no return stmt si it return None
#f2() # error : f2()=None
'''
f2  function
False
f1    function
True
f1    function
None
'''


# Find  outputs 
p=print #  assign ref 'p' to print() function
p('Hyderabad') #  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
#print('Hello') # error : cannot call NoneType
p('Hello') #  call  print()  function  thru  ref  'p'  and   print  'Hello'

'''
o/p:
Hyderabad
Hello'''


# Find   outputs 
x=id # assign  ref  'x'  to  id()  function
print(x(25)) # call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p=len # assign  ref  'p'  to  len()  function
print(p('Hyd')) #  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
'''
o/p:
address of int obj 25
3
'''


# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30))


# Find  outputs 
def  outer():
	print('Outer  function')
	def  inner1():
		print( '1st  inner  function')
	def  inner2():
		print('2nd  inner  function')
	print('Hi')
	inner2()
	print('Hello')
	inner1()
	print('Back  to  outer  function')
# End of the function
print('Begin')
outer()
print('Bye')
'''
o/p:
Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye
'''

# Find  outputs 
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer()
print('Bye')
'''
30
10
Bye
'''

# Find  outputs 
x = 10  #  Gv
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()

'''
o/p:
20
10
'''


# Find  outputs  
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer() # 10


# Find  outputs 
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)
		x +=  7
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  the  function
outer()
print('Bye')
'''
o/p:
10
20
15
Bye
'''