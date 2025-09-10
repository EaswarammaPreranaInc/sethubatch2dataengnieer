#1.  Find  outputs  (Home  work)
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
#print(x) # Error
# 10
# 15
# 20
# 25





#2.  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)
		#nonlocal  x # Error due to nonlocal cannot be used before 'x' used
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
# 10
# 20
# 15





#3.  Find   outputs(Home  work)
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
# 10
# 20
# 15
# 25




#4. Find  outputs(Home  work)
def  outer():
	def  inner():
	   #nonlocal  x # Error due to  we cannot declare nonlocal without Lv in outer function
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	#print(x) # Error due to there is no Lv in outer function
# End  of  the  function
outer()
#print(x) # Error due to there is global x
# 20





#5. Find  outputs(Home  work)
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
# 20
# 25
# 25




#6.  Identify  Error
def   f1():
        #nonlocal   x # Error due nonlocal keyword can be used only in inner function





#7. Find  outputs (Home  work)
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
# 10 20
# 100 200
# 10 20





#8. Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1())# Hello






#9. Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20 # Error due to x is not local variable
		print(x)
	#end of inner function
	gun()
#end of outer function
fun()
# 10






#10.  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		#nonlocal  x # Error due we cannot use global and nonlocal keyword in same function with 'x'
		




#11.  Find  outputs  (Home   work)
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
# 10




#12.  Towers  of  Hanoi
def toh(n, p1, p2, p3):
    if n == 1:
        print(p1, "  --->  ", p3)
    else:
        toh(n - 1, p1, p3, p2) # How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
        print(p1, "  --->  ", p3) # How  to  move  disk  from  pole1  to  pole3
        toh(n - 1, p2, p1, p3) # How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)
n = int(input("How many disks ? : "))
print()
toh(n, 1, 2, 3) 


'''
How many disks ? : 3
1   --->  3
1   --->  2
3   --->  2
1   --->  3
2   --->  1
2   --->  3
1   --->  3
'''
