#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()
f2()
print(f1  is  f2)
f2 = f1
f2()
print(f1  is  f2)
f2 = f1()
print(f2)
f2() # error as we cannot call None

'''
f1 function
f2 function
False
f1 function
True
f1 function 
None
'''

# Find  outputs (Home  work)
p = print # How  to  assign  ref  'p'  to  print()  function
p('Hyderabad') # How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
print = None
print('Hello') # Error as print points to None
p('Hello') # How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'



# Find   outputs (Home  work)
x = id # How  to  assign  ref  'x'  to  id()  function
print(x(25)) # How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p = len # How  to  assign  ref  'p'  to  len()  function
print(p(Hyd)) # How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd


# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a
# End  of  f1  function
print(f1(30)) # 60


# Find  outputs (Home  work)
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
Begin
Outer Function
Hi
2nd inner Function
Hello
1st inner function
Back to outer function
Bye
'''

# Find  outputs  (Home  work)
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

# Find  outputs  (Home   work)
x = 10  #  Gv
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()

'''
20
10
'''

# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer() 

'''
10
'''

# Find  outputs  (Home  work)
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
10
20
15
Bye
'''
