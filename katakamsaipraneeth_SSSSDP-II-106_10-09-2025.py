#  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):
	if  at  least  one  disk:
		How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
		How  to  move  disk  from  pole1  to  pole3
		How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)
# toh( 3 , 1 , 2 , 3)

############# program #################

n = int(input('How many disks ? :   '))
How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate

def  toh(n , p1 , p2 , p3):
    if  n > 0:
        toh(n - 1 , p1 , p3 , p2)
        print(p1 , '  --->  ' , p3)
        toh(n - 1 , p2 , p1 , p3)
# End  of  the  function
toh(n , 1 , 2 , 3)

How many disks ? : 3
1   --->  3
1   --->  2
3   --->  2
1   --->  3
2   --->  1
2   --->  3
1   --->  3


#  Find  outputs  (Home  work)
def  outer():
	x = 10 # lv
	def  inner():
		nonlocal  x # consider x as local
		print(x) # 15
		x = 20 # modifies 15
		print(x) # 20
		x += 5 # 25
	# End  of  inner  function
	print(x) # 10
	x += 5 # 15
	inner() # call fun
	print(x) # 25
# End  of  outer  function
outer() # call fun
print(x) # error


def  outer():
	x = 10 # lv
	def  inner():
		print(x) # error
		#nonlocal  x # error
		x = 20 # lv
		print(x) # 
		x += 5 # 25
	# End  of  inner  function
	print(x) # 10
	x += 5 # 15
	inner()
	print(x) # 15
# End  of  outer  function
outer() # func call


def  outer():
	x = 10 # lv
	def  inner():
		global   x # gv
		x = 20 # gv
		print(x) # 20
		x += 5 # 25
	# End  of  inner  function
	print(x) # 10
	x += 5 # 15
	inner() # fun call
	print(x) # 15
# End  of  outer  function
outer() # fun call
print(x) # 25


# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x # consider  x  as  nonlocal
		x = 20 # modifies  value  of  x  in  outer()
		print(x) # 20
	# End  of  inner  function
	inner()
	print(x) # 20
# End  of  the  function
outer() # 20 20
print(x) # NameError: name 'x' is not defined


# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x # gv
		x = 20 # 20
		print(x) # 20
		x = x + 5 # 25
	# End  of  inner  function
	inner() # fun call
	print(x) # 25
# End  of  the  function
outer() # fun call
print(x) # 25

#  Identify  Error
def   f1():
        nonlocal   x # error

# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a # modifies a
		a = 100 # 10--->100
		b = 200 
		print(a , b) # 100  200
	# End  of  inner  function
	print(a , b) # 10  20
	inner() # fun call
	print(a , b) # 100  20
#end of outer function
outer()


# Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello' # modifies x
	#end of inner function
	f2() # fun call
	return  x # Hello
#  End  of  f1()  function
print(f1()) # Hello


# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20 # error
		print(x) # error
	#end of inner function
	gun()
#end of outer function
fun() # fun call


#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x # x=10 is gv
		nonlocal  x # 20


#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x # 10
		def  f3():
			nonlocal   x # 10
			print(x)
		f3()
	f2()
f1() # fun call