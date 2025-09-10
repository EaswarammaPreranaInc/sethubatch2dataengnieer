#  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):
    #only one disk
    if n==1:
        print(f'move disk from pole {p1} to {p3}')
        return
    #move first n-1 disks from p1 to p2 using p3
    toh(n-1,p1,p3,p2)
    #move the only disk left in p1 to p3
    print(f'move disk from pole {p1} to {p3}')
    #move the n-1 disks from p2 to p3 using p1 
    toh(n-1,p2,p1,p3)
n = int(input('How many disks ? :   '))
toh(n,1,2,3)

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x) 
		x = 20
		print(x) 
		x += 5 #25
	# End  of  inner  function
	print(x)
	x += 5 #15 
	inner()
	print(x)
# End  of  outer  function
outer()
# print(x) #error there is no gloabl 'x'

#10 15 20 25  

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)
		nonlocal  x
		x = 20
		print(x)
		x += 5 #25
	# End  of  inner  function
	print(x)
	x += 5 #15
	inner()
	print(x)
# End  of  outer  function
outer() 

#10 15 20 25

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

# 10 20 10 25

# Find  outputs(Home  work)
def  outer():
	def  inner():
		# nonlocal  x
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	# print(x) #error no 'x' ref
# End  of  the  function
outer()
print(x) #error, no 'x' ref
#20 

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

#20 25 25

#  Identify  Error
def   f1():
        # nonlocal   x
		pass 
#nonlocal can be used only inside a inner function

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
	print(a , b) #10 20
	inner() # 100 200
	print(a , b) #100 20
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
print(f1()) #Hello

# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20 #error, gun does not have 'x'
		print(x)
	#end of inner function
	gun() 
#end of outer function
fun()

#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x 
		nonlocal  x  #no error 
		
#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x 
			print(x) 
		f3()
	f2()#error, f2 does not have any ref 'x'(error is created because of f3)
f1() #error, f2 does not have any ref 'x'(error is created because of f3)