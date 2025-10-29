
#  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):
	if  at  least  one  disk:
		How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
		How  to  move  disk  from  pole1  to  pole3
		How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)

def toh(n,p1,p2,p3):
    if n>0:
        toh(n-1,p1,p3,p2)
        print(f'{p1}----->{p3}')
        toh(n-1,p2,p1,p3)
n = int(input('How many disks ? :   '))
toh(n,1,2,3)

output:-
How many disks ? :   3
1----->3
1----->2
3----->2
1----->3
2----->1
2----->3
1----->3


#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)    # 15
		x = 20
		print(x)    # 20
		x += 5
	# End  of  inner  function
	print(x)    # 10
	x += 5
	inner()
	print(x)    # 25
# End  of  outer  function
outer()
print(x)    # Error x is not defined


#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)    # Error 'x' is used prior to nonlocal declaration
		nonlocal  x
		x = 20
		print(x)    # 20
		x += 5
	# End  of  inner  function
	print(x)    # 10
	x += 5
	inner()
	print(x)    # 25
# End  of  outer  function
outer()


#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)    # 20
		x += 5
	# End  of  inner  function
	print(x)    # 10
	x += 5
	inner()
	print(x)    # 15
# End  of  outer  function
outer()
print(x)    # 25


# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x #Error outer function has no variable x 
		x = 20
		print(x)    # 20
	# End  of  inner  function
	inner()
	print(x)    # Error x is not defined
# End  of  the  function
outer()
print(x)    # x is not defined


# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)    # 20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)    # 25
# End  of  the  function
outer()
print(x)    # 25


#  Identify  Error
def   f1():
        nonlocal   x    #  Error nonlocal should be defined in inner function


# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)    # 100 200
	# End  of  inner  function
	print(a , b)    # 10 20
	inner()
	print(a , b)    # 100 20
#end of outer function
outer()


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
print(f1()) # Hello


# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20   # cannot access local variable before assigning it
		print(x)    # 10
	#end of inner function
	gun()
#end of outer function
fun()


#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x  # Error x is defined as global and nonlocal
		nonlocal  x


#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)    # 10
		f3()
	f2()
f1()
