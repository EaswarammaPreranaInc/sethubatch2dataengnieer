# Find  outputs  (Home  work)
def   f1():
	a = 20 #Here a is the local variable
	print(a) #Prints the value of a i.e 10
	dict = globals() #Globals() is a pre-defined function which returns the dict of all global variables 
	print(dict['a']) #Returns the value of global variable a i.e 10
	a = 30 #Local variable a 
	dict['a'] = 40 #Value of a is modified 11 to 40
#  End  of  f1()  function
a = 10
print(a) #Prints the 10
a += 1 #Here global variable value is increased by 1 i.e a will be 11
f1() #Returns the 10
                # 20
				# 11
print(a) #Here modified global variable value i.e 40



# Find  outputs (Home  work)
x = 10 #Reference x points to 10
def   f1():
	print(x) #Returns value of x i.e 10
	print(globals()['x']) #it converts the global variable x to dict object and prints its value i.e 10
# End of the function
f1() #Here function is called i.e 10
                                # 10



# Find  outputs (Home  work)
def  f1():
	x = 20 #Here x is a local variable points to value 20
	print(x) #Prints the value of x i.e 20
	print(globals()['x']) #Error #Because there is no global variable x
# End  of  the  function
f1()



# Find outputs (Home  work)
def  f1():
	a = 40 #a is a local variable
	b = 50 #b is also local variable
	c = 60 #c is also a local variable
	print(a , b , c) #Prints the value of a, b, c i.e 40 50 60
	dict = globals() #Here we are converting the global variables which are defined outside the function into key-value pairs 
	print(dict['a'] , dict['b'] , dict['c']) #Prints the values of a , b, c i.e 10 20 30
	dict['a'] = 100 #Here we are modifying the value of a i.e 10 to 100
	dict['b'] = 200 #Here we are modifying the value of b i.e 10 to 200
	dict['c'] = 300 #Here we are modifying the value of c i.e 10 to 300
def  f2():
	print(a , b , c) #prints the global variable values a b c we are modified them so modified values are printed i.e 100 200 300 
# End  of  f2  function
a = 10
b = 20
c = 30
f1() #Calling f1 function
f2() #Calling f2 function



# global  keyword  demo  program (Home  work)
def    f1():
	x = 20 #Here x is local variable
	print(x) #Prints the value of x i.e 20 
def   f2():
	global  x #Here we are requesting to treat x as a global variable
	x = 30 #Global Reference x points to 30 
	print(x) #Prints the value of x i.e 30
	x += 1 #Here we are increasing the value of x by 1
def   f3():
	global  y #Here we are requesting to treat y as a global variable 
	y = 40 #Global reference  y points to 40
	print(y) #Prints the value of y
	y += 1 #Here we are increasing the value of y by 1
def   f4():
	x = 50 #Here we are creating a local variable x 
	#global   x #Error #we are already created x as a global variable 
#  End  of  the  functions
x = 10 #Here x is a global variable and points to obj 10
print(x) #prints the value of global variable value i,e 10
x += 1 #Here we are incrementing the global obj 10 by 1 i.e 11
f1() #We are calling f1() function i.e prints 20
print(x) #prints the value of global variable x i.e 11
f2() #Calling f2 function i.e 30
print(x) #Prints the value of x i.e 31
x += 1 #Now we are incrementing x value by 1 i.e 32
f3() #Calling the f3() i.e 40
print(y) #Prints the value of y which is incremented by 1 i.e 41
f4() #Calling the f4() function where we got #Error
print(x) #Prints the value of x i.e 32



# Find outputs (Home  work)
def  f1():
	global  a #Here we are requesting to treat a as global variable
	a = 20 #Here global variable a points to obj 20
	print(a) #Prints the value of a i.e 20
	print(globals()['a']) #Here globals() will convert the global variables into key-value pairs and prints the value of a i.e 20
	a = 30 #Here we are modifying the value of a 20 to 30
# End of the function
a = 10 #Here a is a global variable with value 10
print(a) #Prints the value of a i.e 10
f1() #Calling f1() function prints the 20
									  #20
print(a) #Prints the modified value of a i.e 30



# Find  outputs(Home  work)
def  f1():
	global  a #Here we are requesting treat a as global variable
	#print(a) #Error #as we have not yet created a i.e not defined a 
	a = 10 #Here we have defined the a with value 10
	print(globals()['a']) #Here globals() will convert the global variables into key-value pairs and here it prints the value of a i.e 10
	a = 20 #Here we are modifying the value of a 10 to 20
	print(a) #Prints the value of a i.e 20
	a = 30 #Here we are modifying the value of a 20 to 30
def  f2(): 
	print(a) #Prints the value of global variable a i.e 30
# End  of   f2   function
f1() #Calling the f1() function which prints i.e 10
												#20
f2() #Calling the f2() function which prints i.e 30
print(a) #Prints the global variable value i.e 30



# Find outputs (Home  work)
def  f1():
	global   a #Here we are requesting to treat a as global variable
	a = 10 #Here global variable a is created with value 10
	print(a) #Prints the value of a i.e 10
	a = 20 #Here value of a is modified to 20
def  f2():
	global  a #Here we are requesting to treat a as global variable but already we have global variable a 
	print(a) #printing the value of a i.e 20
	a = 30 #Modifying the value of a 20 to 30
def  f3():
	print(a) #Prints the value of a i.e 30
	globals()['a'] = 40 #Here globals() function will convert the global variables into key-value pairs and here we are modifying a value 30 to 40
# End  of  the  function
f1() #Calling the f1 function i.e 10
f2() #Calling the f2 function i.e 20
f3() #Calling the f3 function i.e 30
print(a) #prints the value of a i.e 40



#  Find  outputs (Home  work)
def  f1():
        a = 10 #Here we are creating a local variable a with value 10
        #global  a #Error #We have already created local variable a and again we are requesting to treat a as global variable
        print(a) #Prints the value of a i.e 10
        global  b #Here we are requesting to treat b as global variable
        b = 20 #Here global variable b is created with value 20
# End  of  f1()  function
f1() #Calling the f1 function i.e 10
print(a) #Error #There is no a defined 
print(b) #Prints the value of b i.e 20




# Find outputs (Home  work)
def  f1():
        global  a #Here we are requesting to treat a as global variable
        print(a) #Prints the value of a i.e 10
        a += 1 #a is incremented by 1 i.e 11
def  f2():
        global  a #Here we are requesting to treat a as global variable
        print(a) #Prints the value of a i.e 11
        a += 1 #a is incremented by 1 i.e 12
# End  of  the  function
a = 10 #Here we have global variable a with value 10
print(a) #Prints the value of a i.e 10
a += 1 #Here we have incremented a by 1 i.e 11
f1() #Calling the f1() function i.e 11
print(a) #Prints the value of a i.e 12
a += 1 #Here we have incremented the value of a i.e 13
f2() #Calling the f2() function i.e 13
print(a) #Prints the value of a i.e 14




# Find  outputs (Home  work)
def   f1():
	a = 20 #Here we have created a local variable a with value 20
	print(a) #Prints the value of a i.e 20 as LV has higher priority than GV
#def  f2():
	#print(a) #Error #As there is no a inside the function 
	#a += 1 #Error #We cannot access the variable a
# End of the function
a = 10 #Here it is a GV with value 10
print(a) #Prints the value of a i,e 10
f1() #Calling the f1() function i.e 20
a += 1 #Here we are incrementing the GV a by 1 i.e 11
#f2() #Error
print(a) #Prints the value of a i.e 11



# Find outputs (Home  work)
def  f1():
	a = 20 #Here we are creating LV a with value 20
	#global   a #Error #As we have already created local variable a again we are trying to create GV 
	print(a) #Prints the value of a i.e 20
	print(globals()['a']) #Here globals() will convert the all Gv into key-value pairs and prints the key of a i.e 10
	a = 30 #Here we are modifying the value of a 10 to 30
	globals()['a'] = 40 #Here we are modifying the key of a to 40
#  End  of  f1()   function
a = 10 #It is a GV with value 10
print(a) #Prints the value of a i.e 10
a += 1 #Here we are incrementing the value of a by 1 i.e 11
f1() #Calling the f1() function i.e 20
								   #11
print(a) #Prints the value of a i.e 40



#  Find   outputs
#def   f1():
	#x = x + 5 #Error #We have not intialized the x and trying to modify it
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5 #Here we are creating a local variable x with value 15
	print(x) #Prints the value of x i.e 15
# End of f2  function
x = 10 #Here it is a GV x with value 10
f1() #Error
f2() #Calling the f2() i.e 15
print(x) #Prints the value of GV x i.e 10