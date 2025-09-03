# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)                           
	dict = globals()
	print(dict['a'])                   
	a = 30
	dict['a'] = 40                     
#  End  of  f1()  function
a = 10
print(a)                               # 10
a += 1                                 # 20
f1()                                   # 11
print(a)                               # 40


# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)                                     # 10
	print(globals()['x'])                        
# End of the function
f1()                                                 # 10



# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)                                     # 20
	print(globals()['x'])                        
# End  of  the  function
f1()                                                 # error 


# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)                                         # 40 50 60
	dict = globals()                                         
	print(dict['a'] , dict['b'] , dict['c'])                 # 10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)                                        # 100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()                                                        
f2()                                                        



# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)                                                    
def   f2():
	global  x
	x = 30
	print(x)                                                    
	x += 1
def   f3():
	global  y
	y = 40
	print(y)                                                    
	y += 1
def   f4():
	x = 50
	global   x
#  End  of  the  functions
x = 10
print(x)                                                       # 10
x += 1                                                         # 11
f1()                                                           # 20
print(x)                                                       # 20
f2()                                                           # 30
print(x)                                                       # 31
x += 1                                                         # 32
f3()                                                           # 40
print(y)                                                       # 41
f4()                                                           # 50 
print(x)                                                       # error because x is assigned to before global 


# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)                                                  
	print(globals()['a'])                                     
	a = 30                                            
# End of the function 
a = 10                                                        # 10
print(a)                                                      # 20
f1()                                                          # 20
print(a)                                                      # 30

                                                      

# Find  outputs(Home  work)
def  f1():
	global  a
	print(a)                                                  # 5
	a = 10
	print(globals()['a'])                                     # 10
	a = 20
	print(a)                                                  
	a = 30                                                    
def  f2():
	print(a)                                                   
# End  of   f2   function
f1()                                                           # 20
f2()                                                           # 30
print(a)                                                       # 30


# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)                                                   
	a = 20
def  f2():
	global  a
	print(a)                                                   
	a = 30
def  f3():
	print(a)                                                   
	globals()['a'] = 40                                         
# End  of  the  function
f1()                                                            # 10
f2()                                                            # 20
f3()                                                            # 30
print(a)                                                        # 40


#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a                                     # a is assigned to before global declaration
        print(a)                                    
        global  b
        b = 20
# End  of  f1()  function
f1()                                                 # 10
print(a)                                             # 10
print(b)                                             # 20




# Find outputs (Home  work)
def  f1():
        global  a
        print(a)                                
        a += 1
def  f2():
        global  a
        print(a)                                 
        a += 1
# End  of  the  function
a = 10                                          #10
print(a)                                        #10
a += 1                                          #11
f1()                                            
print(a)                                        #12
a += 1                                          #13
f2()                                            
print(a)                                        #14



 Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)                                     
def  f2():
	print(a)                                     
	a += 1
# End of the function
a = 10
print(a)                                         #10
f1()                                             #20
a += 1                                           #11
f2()                                             
print(a)                                         # error because local variable a reference before assigned



# Find outputs (Home  work)
def  f1():
	a = 20
	global   a
	print(a)                                      
	print(globals()['a'])                          
	a = 30
	globals()['a'] = 40                              
#  End  of  f1()   function
a = 10
print(a)                                          #10                                     
a += 1                                            #11
f1()                                              # Error because before global a which is not allowed
print(a)                                          



#  Find   outputs
def   f1():
	x = x + 5
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)                                
# End of f2  function
x = 10                                      # create global variable
f1()                                        #error because inside the function  treats as a local variable
f2()                                        
print(x)                                    




 Find outputs (Home  work)
def  f1():
	global   a
	a = 10                                          
	print(a)                                        # 10
	a = 20
def  f2():
	print(a)                                        # 20
	a = 30
	print(a)                                        # 30
def  f3():
	print(a)                                        # 20
	globals()['a'] = 40                             # 40
# End  of  the  function
f1()                                                    # 10
f2()                                                    # 20
f3()                                                    # 30
print(a)                                                # 40