# Towers of Hanoi using recursion

def toh(n, p1, p2, p3):

    if n == 1:   
        print(f"Move disk 1 from pole {p1} to pole {p3}")
        return
    toh(n-1, p1, p3, p2)

    print(f"Move disk {n} from pole {p1} to pole {p3}")
    toh(n-1, p2, p1, p3)

n = int(input("How many disks? : "))

toh(n, 1, 2, 3)
#output:
How many disks? : 3
Move disk 1 from pole 1 to pole 3
Move disk 2 from pole 1 to pole 2
Move disk 1 from pole 3 to pole 2
Move disk 3 from pole 1 to pole 3
Move disk 1 from pole 2 to pole 1
Move disk 2 from pole 2 to pole 3
Move disk 1 from pole 1 to pole 3

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)
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
print(x)#Error
#output:
10
15
20
25

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)#Error
		nonlocal  x#Error
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
#output:
10
20
15

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
#output:
10
20
15
25

# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x # Error
		x = 20
		print(x) # 20
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer() # Error
print(x) # Error

# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)
20
25
25

#  Identify  Error
def   f1():
        nonlocal x # Error

# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)
	# End  of  inner  function
	print(a , b)
	inner()
	print(a , b)
#end of outer function
outer()
10 20
100 200
100 20

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
	def gun():
		x =  x +  20
		print(x)
	#end of inner function
	gun()
#end of outer function
fun() # Error

#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global  x # x global and nonlocal so error
		nonlocal x

#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x) #10
		f3()
	f2()
f1()




















