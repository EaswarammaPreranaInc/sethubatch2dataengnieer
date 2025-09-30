# Find outputs (Home work)
def f1():
    a = 20
    print(a)              #20
    dict = globals()      
    print(dict['a'])      #11
    a = 30                
    dict['a'] = 40        
# End of f1() function
a = 10
print(a)                   #10, from global a
a += 1                     #global variable incremented to 11
f1()                       #20 \n 11 \n
print(a)                   #40


# Find outputs (Home work)
x = 10
def f1():
    print(x)                     #10, from global variable x
    print(globals()['x'])        #
# End of the function
f1()                             #10 \n 10


# Find outputs (Home work)
def f1():
    x = 20                      #local variable x is initialised with 20
    print(x)                    #20
    print(globals()['x'])       #throws error, since there is not gloabal variable x
# End of the function
f1()                            #20 \n error


# Find outputs (Home work)
def f1():
    a = 40                                    #local variable a = 40
    b = 50                                    #local variable b = 50
    c = 60                                    #local variable c = 60
    print(a, b, c)                            #40 <sp> 50 <sp> 60
    dict = globals()
    print(dict['a'], dict['b'], dict['c'])    #10 <sp> 20 <sp> 30
    dict['a'] = 100                           #modifies global variable a to 100
    dict['b'] = 200                           #modifies global variable b to 200
    dict['c'] = 300                           #modifies global variable c to 300
def f2():
    print(a, b, c)                            #prints gloabl variables a, b, c
# End of f2 function
a = 10                                          #global variable a = 10
b = 20                                          #global variable b = 20
c = 30                                          #global variable c = 30
f1()                                            #prints local variables and modifies global variables
f2()                                            #100 <sp> 200 <sp> 300, prints modified global varaibles 

 

# Find outputs (Home work)
def f1():
    global a                      #tells f1 that a is global variable
    a = 20                        #modifies global a to 20
    print(a)                      #20
    print(globals()['a'])         #20
    a = 30                        #modifies global a to 30
# End of the function
a = 10                             #global a
print(a)                           #10
f1()                               
print(a)                           #30


# Find outputs (Home work)
def f1():
    global a                   #declares a as global
    # print(a)                 #error, there is not global variable a
    a = 10                     #creates a global variable a = 10
    print(globals()['a'])      #10
    a = 20                     #modifies global variable to 20
    print(a)                   #20
    a = 30                     #modifies global variable to 30
def f2():
    print(a)                   #30
# End of f2 function 
f1()                           #calls f1()
f2()                           #calls f2()
print(a)                       #30
 

# Find outputs (Home work)
def f1():
    global a                   #tells f1 to treat a as global
    a = 10                     #creates new global variable a = 10
    print(a)                   #10
    a = 20                     #modifies global variable a to 20
def f2():
    global a                   #declares a as global for function f2
    print(a)                   #20
    a = 30                     #modifies global variable a to 30
def f3():
    print(a)                   #30
    globals()['a'] = 40        #modifies global variable a to 40
# End of the function
f1()                            #calls f1
f2()                            #calls f2
f3()                            #calls f3
print(a)                        #40


# Find outputs (Home work)
def f1():
    global a                 #tells a as global for f1
    a = 10                   #creates global variable a = 10
    print(a)                 #10
    a = 20                   #modifies global variable a to 20
def f2():
    # print(a)                 #error, local variable is not yet assigned
    a = 30                   #creates local variable a = 30
    print(a)                 #30
def f3():
    print(a)                 #20
    globals()['a'] = 40      #modifies global variable to 40
# End of the function
f1()                           #calls f1
f2()                           #calls f2
f3()                           #calls f3
print(a)                       #40


# Find outputs (Home work)
def f1():
    a = 10
    # global a                     #cannot declare variable as global after assignment
    print(a)                       #10
    global b                       #declares b as global for f1
    b = 20                         #creates new global variable b = 20
# End of f1() function
f1()                               #calls f1
# print(a)                         #error, there is no global variable a
print(b)                           #20


# Find outputs (Home work)
def f1():
    global a                #declares a as global for f1
    print(a)                #11
    a += 1                  #modifies global variable a to 12
def f2():
    global a                #declares a as global for f2
    print(a)                #13
    a += 1                  #modifies global variable to 14
# End of the function
a = 10                        #global a = 10
print(a)                      #10
a += 1                        #modifies global variable to 11
f1()                          #calls f1
print(a)                      #12
a += 1                        #modifies global varibale to 13
f2()                          #calls f2 
print(a)                      #14


# Find outputs (Home work)
def f1():
    a = 20                         #creates local variable a = 20
    print(a)                       #20
def f2():
    # print(a)                       #error, a is not initialised
    # a += 1                         #error, a is not defined
    pass
# End of the function
a = 10                              #global a = 10
print(a)                            #10
f1()                                #calls f1
a += 1                              #modifies global a to 11
f2()                                #calls f2
print(a)                            #11


# Find outputs (Home work)
def f1():
    a = 20
    # global a                    #cannot declare global after variable is already assigned
    print(a)                      #20
    print(globals()['a'])         #11
    a = 30                        #modifies local variable to 30
    globals()['a'] = 40           #modifies global variable to 40
# End of f1() function
a = 10                            #global variable 10      
print(a)                          #10
a += 1                            #modifies gloabl variable to 11
f1()                              #calls f1
print(a)                          #40


# Find outputs
def f1():
    # x = x + 5                 #error x is not yet defined
    pass
# End of f1 function
def f2():
    x = globals()['x'] + 5    #creates local variable x = 15
    print(x)                  #15
# End of f2 function
x = 10                          #gloabl a = 10
f1()                            #calls f1
f2()                            #calls f2
print(x)                        #10
