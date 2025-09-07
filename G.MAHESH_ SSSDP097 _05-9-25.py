# 1) Find  outputs  (Home  work)

def change(b):
    b.append(25)      # Inside function, prints new list assigned to b
    b[2] = 17         # modifying the list 'b' also modifies the list 'a' 
    del b[1]          
# End of the function
a = [10, 20, 15, 18]
print(a)  # Output: [10, 20, 15, 18]
change(a) # Output: [10, 17, 18, 25]
print(a)  # Output: [10, 17, 18, 25]



# 2) Find  outputs  (Home  work)

def change(b):
    b = [50, 60, 70, 80]
    print(b)
# End of the function
a = [10, 20, 30, 40]
print(a)  # Output: [10, 20, 30, 40]
change(a) # Output: [50, 60, 70, 80]
print(a)  # Output: [10, 20, 30, 40]



# 3) Find  outputs  (Home  work)

def f1(x):
    x = 20
    print(x)         
# End of the function
x = 10
print(x) # Output: 10
f1(x)    # Output: 20
print(x) # Output: 10



# 4) Find  outputs  (Home  work)

def f1(b):
    b[2] = 25         # Error tuple is immutable
# end of the function
a = (10, 20, 15, 18)
print(a) # Output: (10, 20, 15, 18)
f1(a)                 
print(a) # Output: (10, 20, 15, 18)



# 5) Find  outputs (Home  work)

square = lambda x=10: x * x
print(square(5)) # Output: 25
print(square())  # Output: 100


# 6) Find  outputs (Home  work)

print((lambda x: x * x)(7)) # Output: 49
print(lambda x: x * x(7)) # Error x(7) should be defined outside the function
print(lambda x: x * x) # Output: <type and address>
print((lambda x=25: x * x)()) # Output: 625
square = lambda x: x * x
print(square(5)) # Output: 25



# 7) Find  output (Home  work)

add = lambda a, b: a + b   
print(type(add)) # Output: <class 'function'>
print(add(10, 20)) # Output: 30
print(add(10.6, 20.8)) # Output: 31.4
print(add('Hyder', 'abad')) # Output: 'Hyderabad'
print(add(True, False)) # Output: 1
print(add(25, 10.8)) # Output: 35.8
print(add(3+4j, 5+6j)) # Output: (8+10j)
print(add(10, '20')) # Error integer and string cannot be added
print(add()) # Error arguments should be passed
print(add) # Output: <type and address>



# 8) Find  outputs (Home  work)

add = lambda a=1, b=2: a + b
print(add(10, 20)) # Output: 30
print(add()) # Output: 3



# 9) Find  outputs (Home work)

print((lambda x, y: x + y)(10, 20)) # Output: 30
print((lambda x, y: x + y)(10.8, 20.6)) # Output: 31.4
print((lambda x, y: x + y)('Hyder', 'abad')) # Output: 'Hyderabad'
print(lambda x, y: x + y('Hyder', 'abad')) # Error as ('Hyder', 'abad') should be defined outside the function



# 10) Find  outputs (Home  work)

large = lambda a, b: a if a > b else b   
print(large(10, 20)) # Output: 20
print(large(10.7, 5.6)) # Output: 10.7
print(large('g', 's')) # Output: 's'
print(large('Rama', 'Rajesh')) # Output: 'Rajesh'
print(large(True, False)) # Output: True



# 11) Find  outputs (Home  work)

power = lambda a=3.5, b=2: a ** b
print(power(2, 3)) # Output: 8
print(power(4.5, 4)) # Output: 410.06
print(power()) # Output: 12.25
print(power(9)) # Output: 81



# 12) Find  outputs

all = lambda a, b: (a + b, a - b, a * b, a / b)
x = all(10, 7)
print(type(x)) # Output: <class 'tuple'>
print(x) # Output: (17, 3, 70, 1.42)
p, q, r, s = all(9, 2)
print(p) # Output: 11
print(q) # Output: 7
print(r) # Output: 18
print(s) # Output: 4.5



# 13) Find  outputs

a = lambda: 'Hyd'
print(a()) # Output: 'Hyd'
print(a) # Output: <type and address>



# 14) Find  outputs

a = lambda: print('Hyd'); print('Sec'); print('Cyb')
print(a())             
'''
Output:
Hyd
Sec
Cyb
None
'''



# 15) Find  outputs (Home  work)

a = lambda: 'Hyd'; print('Sec'); print('Cyb')
print(a())
'''
Output:
Sec
Cyb
Hyd
'''



# 16) Find  outputs   (Home  work)

a = lambda: print('Hyd'), print('Sec'), print('Cyb')
print(type(a)) # Output: <class 'tuple'>
print(a) # Output: (<type and address>, None, None)
for x in a:
    print(x) 
'''
# Output: 
(<type and address>
None
None
'''
a() # Error tuple object is not callable
print(a[0]()) # Output: Hyd <nextline> None



# 17) Find  outputs  (Home  work)

s = 'Hyd'
print(lambda s: print(s)) # Output: <type and address>
print(lambda x: print(x)(s)) # Error x(s) should be defined outside the function
print((lambda x: print(x))(s)) # Output: Hyd <nextline> None
(lambda x: print(x))(s) # Output: Hyd



# 18) Find outputs  (Home  work)

x = 5
adder1 = lambda y, x=x: x + y
x = 10
adder2 = lambda y, x=x: x + y
x = 20
print(adder1(100)) # Output: 105
print(adder2(200)) # Output: 210
print(adder1(300, 400)) # Error can't send multiple values


# 19) Find  outputs  (Home  work)

a = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
for fun in a:
    print(fun(5))
'''
# Output: 
25
125
625
'''



# 20) Find  outputs

def f1():
    print('Hyd')
def f2():
    print('Sec')
a = [f1, f2]
for x in a:
    x() # Output: Hyd <nextline> Sec
a = [def f1(): print('Hyd'), def f2(): print('Sec')] # Error as we cannot use def inside a list.
print(a) # Error



# 21) Find output  (Home  work)

a = {'power_2': lambda x: x ** 2,
     'power_3': lambda x: x ** 3,
     'power_4': lambda x: x ** 4}
key = 'power_3'
print(a[key]) # Output: <type and address>
print(a ) 
# Output: {'power_2': <type and address>, 'power_3': <type and address>, 'power_4': <type and address>}



# 22) Find  outputs  (Home  work)

def f1(x):
    return lambda n: x ** n
lamb = f1(3)
print(type(f1)) # Output: <class 'function'>
print(type(lamb)) # Output: <class 'function'>
print(lamb(2)) # Output: 9
print(lamb(5)) # Output: 243
print(lamb) # Output: <type and address>
print(lamb()) # Error atleast 1 argument should be send



# 23) Find  outputs   (Home  work)

def eval(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
lam = eval(3, 4, 5)
print(lam(2)) # Output: 25
print(lam(2.5)) # Output: 33.75
print(lam(4)) # Output: 69



# 24) Nested  lambda  function  (Home  work)

add = lambda x=10: lambda y: x + y
a = add()
print(a(20)) # Output: 30
print(add(30)(40)) # Output: 70



# 25) Find  outputs

a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) # Output: [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
c = sorted(a , reverse = True)
print(c) # Output: [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a ,  key =  lambda x : x[1])
print(d) # Output: [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a , key =  lambda x : x[2])
print(e) # Output: [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda x : x[0])
print(f) # Output: [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda x : x[1] , reverse = True)
print(g) # Output: [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1]))   # Error as 'x' is not defined



# 26) Find outputs  (Home  work)

a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
      {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
      {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda x : x['Year'])
print(b) # Output: [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a)) # Error multiple dictonary can't be sorted



# 27) Find outputs  (Home  work)

a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))# Output: (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] ))# Output: (15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] ))# Output: (20, 'Sita', 2800.0)
print(max(a))# Output: (25, 'Kiran', 1500.0)



# 28) Find  output  (Home  work)

add = lambda  x  :   x == 25
print(add(10))# Output: False
add = lambda  x = 25 :   x == 35
print(add())# Output: False
add = lambda  x  :   x = 25 # Error as we cannot assign value to lambda i.e., x=25
add = lambda  x  :   x := 25 # Error as we cannot assign value to lambda i.e., x:=25