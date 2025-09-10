#  Towers  of  Hanoi

def toh(n, source, intermediate, target):
    if n == 0:
        return
    toh(n - 1, source, target, intermediate)
    print(f"{source}   --->  {target}")
    toh(n - 1, intermediate, source, target)

n = int(input('How many disks ? : '))
toh(n, 1, 2, 3)


#  Find  outputs  (Home  work)

def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)       # 15
		x = 20
		print(x)       # 20
		x += 5
	# End  of  inner  function
	print(x)           # 10
	x += 5
	inner()
	print(x)           # 25
# End  of  outer  function
outer()
print(x)               # Error 'x' is not defined outside the function

'''
Outputs:
10
15
20
25
'''


#  Find  outputs  (Home  work)

def outer():
    x = 10
    def inner():
        print(x)      # Error because nonlocal must be declared before using 'x'
        nonlocal x
        x = 20
        print(x)      # 20
        x += 5
    print(x)          # 10   
    x += 5
    inner()
    print(x)          # 25
outer()               # Error 'x' is not defined outside the function


#  Find   outputs(Home  work)

def outer():
    x = 10
    def inner():
        global x
        x = 20
        print(x)      # 20
        x += 5        # 25
    print(x)          # 10
    x += 5            # 15 
    inner()
    print(x)          # 15
outer()
print(x)              # 25 


'''
Output:
10
20
15
25
'''


#  Find outputs(Home  work)

def outer():
    def inner():
        #nonlocal x
        x = 20
        print(x) # 20
    inner()
    print(x)  # x is not defined 
outer()
print(x)     # x is not defined globally


#  Find outputs(Home  work)

def outer():
    def inner():
        global x
        x = 20
        print(x)
        x = x + 5
    inner()
    print(x)

outer()
print(x)

'''
Output:
20
25
25
'''


#  Identify  Error

def   f1():
    #nonlocal x

# Error: x is not defined in any outer function


# Find  outputs (Home  work)

#def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200                  # Error because b is treated as local variable without declaration
		print(a , b)             # 100 20
	# End  of  inner  function
	print(a , b)                 # 10 20
	inner()
	print(a , b)                 # 100 20
#end of outer function
outer()

'''
Outputs:
10 20
100 20
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
print(f1())                  # Hello


# Find  output(Home  work)

def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x)            # x is not defined
	#end of inner function
	gun()
#end of outer function
fun()


#  Identify  Error

x = 10
def   outer():
	x = 20
	def  inner():
		global  x
		#nonlocal x        # we can't declare global and nonlocal in a same function

#  Find  outputs  (Home   work)

def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)       # 10
		f3()
	f2()
f1()





