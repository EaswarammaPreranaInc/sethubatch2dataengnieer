# 5) Find  outputs 
square = lambda  x = 10  :   x * x
print(square(5)) #25
print(square())  #100





# 6)Find  outputs  
print((lambda   x  :  x*x) (7))#49
print( lambda   x  :  x * x(7))#<function <lambda> at <address of the function>>
print( lambda   x  :  x * x) #<function <lambda> at<address of the function>>
print( (lambda  x = 25 : x*x)() )#625
square = lambda  x :  x  *  x
print(square(5))#25





# 7)Find  output 
#How  to  define  lambda  function   to  return  sum   of  two  arguments
add = lambda x, y : x+y
print(type(add)) #<class 'function'>
print(add(10 , 20))#30
print(add(10.6 , 20.8))#31.4
print(add('Hyder', 'abad')) #Hyderabad
print(add(True , False))#1
print(add(25 , 10.8))#35.8
print(add(3 + 4j, 5 + 6j))#8+10j
#print(add(10 , '20'))  #Throws error as int and str can't be added or concatenated 
#print(add())#Throws error as add expects 2 arguments
print(add)#<function add at <address of lambda function>>





# 8) Find  outputs 
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) #30
print(add())#3





# 9) Find  outputs
print((lambda  x , y : x + y) (10 , 20) )  #30
print((lambda  x , y : x + y) (10.8 , 20.6))  #31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad'))  #Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))#<function <lambda> at <address of lambda function>>





# 10) Find  outputs 
#How  to  define  lambda  to  detrmine  largest  of  two  arguments
large = lambda x, y : x if x>y else y
print(large(10  ,  20))   #20
print(large(10.7  ,  5.6))   #10.7
print(large('g'  ,  's')) #s
print(large('Rama', 'Rajesh')) #Rama
print(large(True  ,  False)) #True





#11) Find  outputs 
power = lambda a = 3.5, b = 2 : a**b
print(power(2 , 3))#8           
print(power(4.5, 4))#410.06
print(power())#12.25
print(power(9)) #81





# 12) Find  outputs
all = lambda a, b : (a + b, a - b, a * b, a / b)
x = all(10 , 7)
print(type(x)) #<class 'tuple'>
print(x)  #(17, 3, 70, 1.42)
p , q , r , s = all(9 , 2)
print(p) #11
print(q) #7
print(r) #18
print(s) #4.5





# 13)  Find  outputs
a  =  lambda : 'Hyd'
print(a())#Hyd
print(a)#<function <lambda> at <address of lambda function>>





# 14)Find  outputs
a  =  lambda : print('Hyd') ;  print('Sec');  print('Cyb')
print(a())   #Sec<next_line>Cyb<next_line>Hyd<next_line>None




#15) Find  outputs 
a = lambda : 'Hyd'; print('Sec'); print('Cyb')
print(a()) #Sec<next_line>Cyb<next_line>Hyd





# 16) Find  outputs  
a = lambda : print('Hyd'), print('Sec'), print('Cyb')
print(type(a)) #<class 'tuple'>
print(a)#(<function <lambda> at <address of the lambda function>>, None, None)
for  x  in  a:
	print(x)   #<function <lambda> at <address of lambda function>><next_line>None<next_line>None
#a()      #Throws error as tuple is not callable
print(a[0]())  #hyd<next_line>None





# 17)  Find  outputs  
s = 'Hyd'
print(lambda s : print(s))#<function <lambda> at <address of the lambda function>>
print(lambda x  : print(x)(s)) #<function <lambda> at <address of the lambda function>>
print((lambda x : print(x))(s))#Hyd<next_line>None
(lambda x : print(x)) (s)  #Hyd





#18)  Find outputs  
x = 5
adder1 = lambda y, x = x : x + y
x = 10
adder2 = lambda y, x = x : x + y
x = 20
print(adder1(100))#105
print(adder2(200)) #210
print(adder1(300 , 400))#700





# 19) Find  outputs  
a = [lambda x : x*2, lambda x : x*3, lambda x : x**4]
for  fun   in   a:
    print(fun(5))#10<next_line>15<next_line>625





# 20)  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1,f2]
for  x  in  a:
	     x()  #hyd<nextline>Sec
#a = [def f1(): print('Hyd'), def f2(): print('Sec')] #Error
print(a)#[<function f1 at <address of the f1 function>>,<function f2 at <address of the f2 function>>]





#21)  Find output  
a = {'power_2'  :  lambda   x  :  x ** 2 ,
     'power_3'  :  lambda   x  :  x ** 3 ,
  	 'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])#<function <lambda> at <address of the 2nd lambda function>>
print(a[key](5)) #125





# 22) Find  outputs 
def   f1(x):
        return lambda n : x**n
lamb = f1(3)
print(type(f1))  #<class function>
print(type(lamb)) #<class function>
print(lamb(2))  #9
print(lamb(5)) #243
print(lamb) #<function <lambda> at <address of the lambda function>>
#print(lamb())    #Throws error as we aren't passing any arguments to the lambda function





# 23) Find  outputs   
def   eval(a , b , c):
        return  lambda x : a * x**2 + b * x + c
lam = eval(3, 4, 5)
print(lam(2))   #25
print(lam(2.5))   #33.75
print(lam(4))    #69





#24 Nested  lambda  function
add  =  lambda x=10 :  lambda y : x + y
a = add()
print(a(20))  #30
print(add(30)(40)) #70





# 26) Find  outputs
a= ((10, 'Rama', 1000.0), (20, 'Sita', 2000.0), (15,'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0))
b = sorted(a)
print(b)#[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
c = sorted(a, reverse = True)
print(c)#[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a, key =  lambda x : x[1])
print(d)#[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a, key = lambda x : x[2])
print(e)#[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a, key = lambda x : x[0])
print(f) #[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a, key=lambda x : x[1], reverse=True)            
print(g)#[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
#print(sorted(a , key = x[1]))   #Throws error as there is no x





#27) Find outputs  
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) #[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
#print(sorted(a)) #Throws error as dictionaries can't be sorted





# 28)Find outputs  
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a, key = lambda x : x[0])) #(25, 'Kiran', 1500.0)
print(max(a, key = lambda x : x[1]))#(15, 'Vamsi', 2000.0)
print(max(a, key = lambda x : x[2]))  #(20, 'Sita', 2800.0)
print(max(a)) #(25, 'Kiran', 1500.0)





#29) Find  output  
add = lambda x : x == 25
print(add(10)) #False
add = lambda x = 25 : x == 35
print(add())   #False
#add = lambda  x  :   x = 25#Throws error as lambda can't modify the argument
#add = lambda  x  :   x := 25 #Throws error as lambda can't modify the argument  
