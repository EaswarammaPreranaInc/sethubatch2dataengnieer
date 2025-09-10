#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)#15
		x = 20
		print(x)#20
		x += 5#25
	# End  of  inner  function
	print(x)#10
	x += 5 #15
	inner()
	print(x)#25
# End  of  outer  function
outer()
#print(x)#error cannot defined
'''
10
15
20
25
'''

#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x#15
		x = 20
		print(x)#20
		x += 5
	# End  of  inner  function
	print(x)#10
	x += 5#15
	inner()
	print(x)#25
# End  of  outer  function
outer()
print(x)
'''
10
20
15
25
'''

#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
print(x)
'''
10
20
15
25
'''


# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x#error due there is  no variable in outer function
		x = 20
		print(x)#20
	# End  of  inner  function
	inner()
	print(x)#x is not defined
# End  of  the  function
outer()
print(x)#error x is not defined



# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)#20
		x = x + 5#25
	# End  of  inner  function
	inner()
	print(x)#25
# End  of  the  function
outer()
print(x)#25
'''
20
25
25
'''


#  Identify  Error
def   f1():
       # nonlocal   x#error due nonlocal variable only inner function
	   pass
		

# Find  outputs (Home  work)
# Find  outputs (Home  work)
def outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)#(100,200)
	# End  of  inner  function
	print(a , b)#(10,20)
	inner()
	print(a , b)#(100,20)
#end of outer function
outer()
'''
10 20
100 200
100 20
'''

# Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1())#Hello


# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20#error due  to without nonlocal variable x cannot modified
		print(x)#10
	#end of inner function
	gun()
#end of outer function
fun()
'''
10
'''


#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		#global   x
		nonlocal  x#error python does n't allow both global and non local variblesin the same scope
		

#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)
		f3()
	f2()
f1()
'''
10
10
'''


#  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):
	if  n>=1:
            toh(n-1,p1,p3,p2)#How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
            print(f'{p1}----->{p3}')
            toh(n-1,p2,p1,p3)
	
		
# toh( 3 , 1 , 2 , 3)
n = int(input('How many disks ? :   '))
toh(n,1,2,3)
#How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate