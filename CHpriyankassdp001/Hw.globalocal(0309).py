1.

# Find  outputs  (Home  work)
def   f1():
	a = 20#local variable
	print(a)#20
	dict = globals()#dict of global variables
	print(dict['a'])#11
	a = 30#local variable
	dict['a'] = 40#modiefies the global variable to 40
#  End  of  f1()  function
a = 10#global variable
print(a)# 10
a += 1 #increment 10+1=11
f1()# call the f1 function
print(a)#40

2
# Find  outputs (Home  work)
x = 10# global variable
def   f1():
	print(x)#10
	print(globals()['x'])
# End of the function
f1()# function call

3

# Find  outputs (Home  work)
def  f1():#function header
	x = 20#local variable due to inside the function
	print(x)#20
	print(globals()['x'])#{} due to there is no global variables and global funtion takes dict of key value pairs
# End  of  the  function
f1()#function call

4

# Find outputs (Home  work)
def  f1():
	a = 40## local variable
	b = 50# local variable
	c = 60# local variable
	print(a , b , c)#40 50 60
	dict = globals()# dictionary of global variables
	print(dict['a'] , dict['b'] , dict['c'])#10 20 30
	dict['a'] = 100#modifies the global variable
	dict['b'] = 200#modifies the global variable
	dict['c'] = 300#modifies the global variable
def  f2():
	print(a , b , c)# 100 200 300
# End  of  f2  function
a = 10# Global variable
b = 20# Global variable
c = 30# Global variable
f1()# call the f1 function
f2()# call the f2 function

5


# global  keyword  demo  program (Home  work)
def    f1():
	x = 20# local variable
	print(x)#20
def   f2():
	global  x #request the f2 function to x consider as global variable
	x = 30  # global variable for this function
	print(x) #30
	x += 1 #30+1=31
def   f3():
	global  y	#request the f3 function to y consider as global variable
	y = 40	# global variable
	print(y)	#40
	y += 1	#40+1=41
def   f4():
	x = 50	#local variable
	#global   x	#not valid
#  End  of  the  functions
x = 10  #Global variable
print(x)#10
x += 1# 10+1=11
f1()#call the f1 function
print(x)#11
f2()# call the f2 function
print(x)#31
x += 1	#31+1=32
f3()	#call the f3 function
print(y)	#41
f4()	#call the f4 function
print(x)	#32


6

# Find outputs (Home  work)
def  f1():
	global  a	#request the f1 function for consider the a as global variable
	a = 20	#global variable
	print(a)	#20
	print(globals()['a'])	#20
	a = 30	#modifies the Variable
# End of the function
a = 10 	#global variable
print(a)	#10
f1()	#call the f1 function
print(a)	#30

7
# Find  outputs(Home  work)
def  f1():
	global  a	#reques the function for a consider as the global variable
	#print(a)
	a = 10	#global variable
	print(globals()['a'])	#10 globals() returns the global variables as dictionary of key value pairs
	a = 20	#Modifies the a value
	print(a)	#20
	a = 30	#again modifies the value and it is global not local
def  f2():
	print(a)	#30
# End  of   f2   function
f1()	# call the f1 function
f2()	#call the f2 function
print(a) #30

8

# Find outputs (Home  work)
def  f1():
	global   a	#request the  funtion a consider as the global variable
	a = 10	#global variable
	print(a) 	#10
	a = 20	#modifies the gv to 20
def  f2():
	global  a	#request the  funtion a consider as the global variable
	print(a)	#20 Here we take 20 becuase it act as gobal variable
	a = 30	#global variable modifies to 30
def  f3():
	print(a)	#30
	globals()['a'] = 40	#modifies the value of a key of global variable
# End  of  the  function
f1()	#call the f1 function
f2()	#call the f2 function
f3()	#call the f3 function
print(a)	#40

#9


# Find outputs (Home  work)
def  f1():
	global   a	# it request the function for a consider as global variable
	a = 10	#gv(global variable)
	print(a)	#10
	a = 20	#modifies the gv to 20
def  f2():
	#print(a)	#Error due to a is not defined
	a = 30	#local variable
	print(a)	#30
def  f3():
	print(a)	#30
	globals()['a'] = 40	#modifies the gv to 40
# End  of  the  function
f1()	#call the function f1
f2()	#call the f2 function
f3()	#call the f3 function
print(a)	#40

10
#  Find  outputs (Home  work)
def  f1():
        a = 10	#local variable
        #global  a	#not valid
        print(a)	#10
        global  b	#request the function to b consider ass gv
        b = 20		#gv
# End  of  f1()  function
f1()	#call the f1 function
#print(a)	##error
print(b)	#20

11

# Find outputs (Home  work)
def  f1():
        global  a	#a consider as the global varaible
        print(a)	#11
        a += 1		#11+1=12
def  f2():
        global  a	#a consider as the global varaible
        print(a)	#13
        a += 1		#13+1=14
# End  of  the  function
a = 10	#global variable
print(a)	#10
a += 1	#10+1=11
f1()	#call the f1 function
print(a)	#12
a += 1	#12+1=13
f2()	#call the f2 function
print(a)	#14

12

 # Find  outputs (Home  work)
def   f1():
    a = 20	#local variable
    print(a)	#20
#def  f2():
    #print(a)	#Error due to there is no local variable but it not take global var becuase here a+=1 is present so it thinks the local variable is here
    #a += 1	#11+1=12 but no use
# End of the function
a = 10	#global variable
print(a)	#10
f1()	#call the f1 function
a += 1	#10+1=11
#f2()	#call the f2 function
print(a)	#11

13

# Find outputs (Home  work)
def  f1():
	a = 20	#local variable
	#global   a	#not valid
	print(a)	#20
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10	#global variable
print(a)	#10
a += 1	#10+1=11
f1()	#call the function f1
print(a)

14
#  Find   outputs
#def   f1():
	#x = x + 5	#not valid because there is no local variable
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5  #x=10+5=15
	print(x)#15
# End of f2  function
x = 10	#global variable
#f1()	#call the function f1
f2()	#call the function f2
print(x)#10