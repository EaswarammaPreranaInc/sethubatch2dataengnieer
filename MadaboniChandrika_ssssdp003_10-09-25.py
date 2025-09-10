#2nd program
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x) #15 (outer fun x value)
		x = 20  #updated to 20
		print(x) #20
		x += 5 #incremented further by 5-->25
	# End  of  inner  function
	print(x)#10
	x += 5 #outer fun x is incremented to 15
	inner() #15 \n 20
	print(x)#25
# End  of  outer  function
outer()
#print(x) #error,x is not defined


#3rd program
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)#error, x is used before defination
		nonlocal  x #treats x as outer func variable
		x = 20 #x now modified to 20
		print(x) #20
		x += 5 #20 incremented to 25
	# End  of  inner  function
	print(x)#10
	x += 5 #x incremented by 5 -->15
	inner() #20
	print(x)#25
# End  of  outer  function
outer()


#4th program
#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20 #GV x with 20 is created
		print(x) #GV -> 20 
		x += 5  #GV modified to 25
	# End  of  inner  function
	print(x) #10
	x += 5 #15
	inner()#20
	print(x) #15 , as x is modified in line 11
# End  of  outer  function
outer()
print(x) # GV ->25 ,as it is outside function


#5th program
# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x #error, as there is no variable x in outer func
		x = 20 
		print(x) #20
	# End  of  inner  function
	inner()#20
	#print(x) #error,x not defined
# End  of  the  function
outer()
#print(x) #error, x not defined globally


#6th program
# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x #x is treated as GV
		x = 20  #x obj is created with value 20
		print(x) #20
		x = x + 5 #25
	# End  of  inner  function
	inner()#20
	print(x)#25
# End  of  the  function
outer()
print(x)#25


#7th program
#  Identify  Error
def   f1():
        #nonlocal   x # error, nonlocal keyword cannot be used in the outer function f1
        pass


#8th program
# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a  #treat a as outer func LV
		a = 100
		b = 200
		print(a , b)#100 200
	# End  of  inner  function
	print(a , b)#10 20
	inner()
	print(a , b)#100 20
#end of outer function
outer()


#9th program
# Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x #treats x as func f1 LV
		x =  'Hello' #x modified to Hello
	#end of inner function
	f2()
	return  x #Hello
#  End  of  f1()  function
print(f1()) #Hello


#10th program
# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20 #error ,x is not intialised
		print(x) #10, outer fun x value is considered
	#end of inner function
	gun()
#end of outer function
fun()


#11th program
#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		#global   x # x cannot be both nonlocal and global
		nonlocal  x


#12th program
#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)#10
		f3()
	f2()
f1()