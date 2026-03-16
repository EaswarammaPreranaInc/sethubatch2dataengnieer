'''
#  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):
	if  at  least  one  disk:
		How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
		How  to  move  disk  from  pole1  to  pole3
		How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)
# toh( 3 , 1 , 2 , 3)
n = int(input('How many disks ? :   '))
How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate
How many disks ? : 3
1   --->  3
1   --->  2
3   --->  2
1   --->  3
2   --->  1
2   --->  3
1   --->  3
'''
#  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):
	if n > 0:
		toh(n-1,p1,p3,p2) #How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
		print(f'{p1} -----> {p3}') #How  to  move  disk  from  pole1  to  pole3
		toh(n-1,p2,p1,p3) #How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)
# toh( 3 , 1 , 2 , 3)
n = int(input('How many disks ? :   '))
toh(n,1,2,3)#How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate
'''output:
How many disks ? :   3
1 -----> 3
1 -----> 2
3 -----> 2
1 -----> 3
2 -----> 1
2 -----> 3
1 -----> 3
'''


#  Find  outputs  (Home  work)
def  outer():
	x = 10 #X is the LV of outer function
	def  inner():
		nonlocal  x #Here we are requesting to treat x as LV of outer function
		print(x) #15
		x = 20
		print(x) #20 #As x is modified to 20 
		x += 5 #Here x is modified to 25
	# End  of  inner  function
	print(x) #10 #as we are printing the x before inner function call
	x += 5 #Here we are modifying x to 15
	inner()
	print(x) #25
# End  of  outer  function
outer()
print(x) #Error #x is not defined
'''outputs:
10
15
20
25
'''


#  Find  outputs  (Home  work)
def  outer():
	x = 10 #x is the LV of outer function
	def  inner():
		#print(x) #Error #As the we are printing the x before declaration and we asking to treat x has LV of outer function in the next line
		nonlocal  x #Here we are asking to treat x as LV of outer function
		x = 20 #Here x is modified to 20
		print(x) #Print the value of x i.e 20
		x += 5 #25 
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
'''output:
10
20
25
'''


#  Find   outputs(Home  work)
def  outer():
	x = 10 #LV x with value 10 is the LV of outer function 
	def  inner(): 
		global   x #Requesting to treat x as global variable 
		x = 20 #Here global variable x is created
		print(x) #Printing the x i.e 20
		x += 5 #Incrementing the x by 5 i.e 25
	# End  of  inner  function
	print(x) #Printing the x before calling the inner function so output is i.e 10
	x += 5 #Modifying the x 10 to 15
	inner() #Inner function is called 
	print(x) #X of outer function LV is printed i.e 15
# End  of  outer  function
outer()
print(x) #Prints the global variable x value i.e 25
'''outputs:
10
20
15
25
'''


# Find  outputs(Home  work)
def  outer(): #Here outer function is defined
	def  inner(): #Inside outer function inner function is defined 
		#nonlocal  x #Error # nonlocal x keyword is used when there is LV x is defined in the outer function only 
		x = 20 #This is the LV of inner function
		print(x) #Prints the value of x in the inner function i.e 20
	# End  of  inner  function
	inner() #Here inner function is called
	print(x) #Error #There is no LV x is defined in the outer function
# End  of  the  function
outer() #Here outer function is called
print(x) #Error there is no GV x



# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x #Here we are requesting to treat x as global variable
		x = 20 #Here GV is created with value 20
		print(x) #Prints the value of x i.e 20
		x = x + 5 #Here Gv x is modified to 25
	# End  of  inner  function
	inner() 
	print(x) #Prints the value of x i.e 25
# End  of  the  function
outer()
print(x) #Prints the value of x i.e 25
'''output:
20
25
25
'''


#  Identify  Error
def   f1():
        #nonlocal x # Here nonlocal keyword should be used only in the nested function in the inner function but here there is no inner function



# Find  outputs (Home  work)
def outer():
	a = 10 
	b = 20
	def inner():
		nonlocal a #Here we are requesting to treat a as local variable of outer function
		a = 100 #So here a is modified from 10 to 100
		b = 200
		print(a , b) #Prints the value of a , b i.e 100 200
	#End  of  inner  function
	print(a , b) #Prints the value of a , b i.e 10 20
	inner() #Inner function is called
	print(a , b) #After inner function called value of a is modified to 100 i.e 100 20
#end of outer function
outer()
'''outputs:
10 20
100 200
100 20
'''


# Find  outputs (Home  work)
def   f1():
	x = 'John' #Initially x points to str 'John'
	def  f2():
		nonlocal  x #Here we are requesting to treat x as LV of outer function 
		x =  'Hello' #So here x is modified from str 'John' to 'Hello'
	#end of inner function
	f2()
	return  x #Here f1 is returning x i.e Hello
#  End  of  f1()  function
print(f1()) #Prints the str Hello
'''outputs:
Hello
'''


# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20 #Error #here python thinks that x is a local variable of gun function and tries to evaluate the x+20 but we have not initialized the x value 
		print(x) #Prints the value of x which is defined in the fun() i.e 10
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
		#nonlocal  x #Error #Because we have already made x as a GV and again we are requesting to treat x has local variable of outer function


#  Find  outputs  (Home   work)
def   f1():
	x = 10 #x is the LV of the f1 function
	def  f2():
		nonlocal   x #Here in the f2 function we are asking to treat x as local variable of f1 function
		def  f3():
			nonlocal   x #Here we are asking to treat x as local variable of f2 function 
			print(x) #Prints the value of x i.e 10
		f3()
	f2()
f1()
'''output:
10
'''