# 1) Towers  of  Hanoi

def toh(n, p1, p2, p3):
    if n == 0:
        return
    toh(n - 1, p1, p3, p2) # How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
    print(f"{p1}  --->  {p3}") # How  to  move  disk  from  pole1  to  pole3
    toh(n - 1, p2, p1, p3) # How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)

n = int(input('How many disks ? : '))
toh(n, 1, 2, 3)

'''
Output:
How many disks ? : 4
1  --->  2
1  --->  3
2  --->  3
1  --->  2
3  --->  1
3  --->  2
1  --->  2
1  --->  3
2  --->  3
2  --->  1
3  --->  1
2  --->  3
1  --->  2
1  --->  3
2  --->  3
'''



# 2) Find  outputs  (Home  work)

def  outer():
	x = 10
	def  inner():
		nonlocal  x # nonlocal treats 'x' as local variable of inner fuction
		print(x)    # 15
		x = 20
		print(x)    # 20
		x += 5      # x=20+5=25
	# End  of  inner  function
	print(x)        # 10
	x += 5          # x=10+5=20
	inner()
	print(x)        # 25
# End  of  outer  function
outer()             
print(x)            # Error as 'x' is not defined outside the function
'''
Outputs:
10
15
20
25
'''



# 3) Find  outputs  (Home  work)

def outer():
    x = 10
    def inner():
        print(x)    # Error because nonlocal must be declared before using 'x'
        nonlocal x
        x = 20
        print(x)    # 20
        x += 5
    print(x)        # 10   
    x += 5
    inner()
    print(x)        # 25
outer()            
'''
Output:
10
20
25
'''



# 4) Find   outputs(Home  work)

def outer():
    x = 10
    def inner():
        global x        
        x = 20
        print(x)      # 20
        x += 5        # x=20+5=25
    print(x)          # 10
    x += 5            # x=10+5=15 
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


# 5) Find outputs(Home  work)

def outer():
    def inner():
        nonlocal x # Error as local variable 'x' is not there in outer fuction
        x = 20
        print(x) # 20
    inner()
    print(x)  # Error as 'x' is not defined 
outer()
print(x)     # Error as 'x' is not defined globally



# 6) Find outputs(Home  work)

def outer():
    def inner():
        global x    # Creates a global variable 'x' with value 20
        x = 20
        print(x)    # 20
        x = x + 5   # x=20+5=25
    inner()
    print(x)        # 25
outer()
print(x)            # 25

'''
Output:
20
25
25
'''


 
# 7) Identify  Error

def   f1():
    nonlocal x     # Error: x is not defined in any outer function



# 8) Find  outputs (Home  work)

def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a    # treat 'a' as local varible of outer fuction
		a = 100         # 'a' is modified to 100
		b = 200         # creates a new local variable b in inner fuction
		print(a , b)    # 100 200
	# End  of  inner  function
	print(a , b)        # 10 20
	inner()
	print(a , b)        # 100 20
#end of outer function
outer()

'''
Outputs:
10 20
100 200
100 20
'''



# 9) Find  outputs (Home  work)

def   f1():
	x = 'John'
	def  f2():
		nonlocal  x 
		x =  'Hello' #'x' is modified to 'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1())         # Output: Hello



# 10) Find  output(Home  work)

def  fun():
	x = 10
	def  gun():
		x =  x +  20
		print(x)    # error as 'x' is not defined in the inner fuction
	#end of inner function
	gun()
#end of outer function
fun()



# 11) Identify  Error

x = 10
def   outer():
	x = 20
	def  inner():
		global  x
		nonlocal x        # we can't declare global and nonlocal in a same function



# 12) Find  outputs  (Home   work)

def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)       # output: 10
		f3()
	f2()
f1()




