#  Towers  of  Hanoi
# def  toh(n , p1 , p2 , p3):
# 	if  at  least  one  disk:
# 		How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
# 		How  to  move  disk  from  pole1  to  pole3
# 		How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)
# # toh( 3 , 1 , 2 , 3)
# n = int(input('How many disks ? :   '))
# How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate

def toh(n, p1, p2, p3):
    if n == 1:
        print(f"{p1}   --->  {p3}")
    if n > 1:
        toh(n-1, p1, p3, p2)
        print(f"{p1}   --->  {p3}")
        toh(n-1, p2, p1, p3)

n = int(input("How many disks ? : "))
toh(n, 1, 2, 3)



#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)  #  15
		x = 20
		print(x)  #  20
		x += 5  #  25
	# End  of  inner  function
	print(x)  #  10
	x += 5  #  15
	inner()
	print(x)  #  25
# End  of  outer  function
outer()
print(x)  #  Error due to x is not defined in outer function



#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)  #  15
		nonlocal  x
		x = 20
		print(x)  #  20
		x += 5  #  x=25
	# End  of  inner  function
	print(x)  #  10
	x += 5  #  x=15
	inner()
	print(x)  #  25
# End  of  outer  function
outer()



#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)  #  20
		x += 5  #  25
	# End  of  inner  function
	print(x)  #  10
	x += 5  #  15
	inner()
	print(x)  #  15
# End  of  outer  function
outer()
print(x)  #  25




# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x  #  Error due to no x in outer function
		x = 20
		print(x)  #  20
	# End  of  inner  function
	inner()
	print(x)  #  Error due to x is not defined
# End  of  the  function
outer()
print(x)  #  Error due to x is not defined



# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)  #  20 
		x = x + 5  #  25
	# End  of  inner  function
	inner()
	print(x)  #  25
# End  of  the  function
outer()
print(x)  #  25



#  Identify  Error
def   f1():
        nonlocal   x  # Eror due to nonlocal use only inner function


# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)  #  100 200
	# End  of  inner  function
	print(a , b)  #  10 20
	inner()
	print(a , b)  #  100 20
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
	return  x  #  Hello
#  End  of  f1()  function
print(f1())



# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20  #  Error
		print(x)  
	#end of inner function
	gun()
#end of outer function
fun()


#  Identify  Error
x = 10
def   outer():  #  Outer fun not called
	x = 20
	def  inner():  #  inner fun not called
		global   x
		nonlocal  x


#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)  #  10
		f3()
	f2()
f1()
