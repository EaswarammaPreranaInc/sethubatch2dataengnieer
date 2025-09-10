: #  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):
	if  at  least  one  disk:
		How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
		How  to  move  disk  from  pole1  to  pole3
		How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)
# toh( 3 , 1 , 2 , 3)
n = int(input('How many disks ? :   '))
How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate
#################
def toh(n, p1, p2, p3):
    if n > 0:   # at least one disk
        toh(n-1, p1, p3, p2)   # move n-1 disks from p1 → p2 using p3
        print(f"Move disk {n} from pole {p1} to pole {p3}")   # move main disk
        toh(n-1, p2, p1, p3)   # move n-1 disks from p2 → p3 using p1

n = int(input("How many disks? : "))
toh(n, 1, 2, 3)





: #  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)    # 15
		x = 20
		print(x)    # 20
		x += 5      # x=25
	# End  of  inner  function
	print(x)  # 10
	x += 5    # x=25
	inner()
	print(x) # 25
# End  of  outer  function
outer()
print(x) # error

###########
10
15
20
25
NameError: name 'x' is not defined




: #  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)
		nonlocal  x
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
############

Python reads function body before execution.

It sees nonlocal x → all references to x are treated as "nonlocal".

But print(x) appears before the declaration →  SyntaxError.




: #  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x) # 20
		x += 5   # 25
	# End  of  inner  function
	print(x)  # 10
	x += 5    # 15
	inner()
	print(x)  # 15
# End  of  outer  function
outer()
print(x) # 25
###########
10
15
20
15
25






: # Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)
###SyntaxError: no binding for nonlocal 'x' found.



: # Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)   # 20
		x = x + 5  # 25
	# End  of  inner  function
	inner()
	print(x)  # 25
# End  of  the  function
outer()
print(x) # 25
############
20
25
25




: #  Identify  Error
def   f1():
        nonlocal   x
### Error → SyntaxError: nonlocal declaration not allowed at module level.



: # Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b) # 100 200
	# End  of  inner  function
	print(a , b)  # 10 20
	inner()
	print(a , b)  # 100  20
#end of outer function
outer()
###############
10 20
100 200
100 20




: # Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1())
#############
Hello



: # Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x)
	#end of inner function
	gun()
#end of outer function
fun()
#### UnboundLocalError.



: #  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x
### Error → cannot use both global and nonlocal on the same variable.



: #  Find  outputs  (Home   work)
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
###########
10
