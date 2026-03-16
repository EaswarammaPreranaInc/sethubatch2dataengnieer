#  Find  outputs  (Home  work)
def  change(b):
	b . append(25) 		# Here we are appending 25 to the list
	b[2] = 17 			# And upadating the 2nd index value to 17 
	del  b[1] 			# deleting the value of index 1
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) 				# Prints the list a i.e [10, 20, 15, 18]
change(a) 				# Here function is called with global variable a so function modifies the list a
print(a) 				# prints the list with [10, 17, 18, 25]

'''
1)  a = [10 , 20 , 15 , 18]
    change(a)
    What  is   passed  to  change()  function ? ---> List  itself  but  not  elements  of  list

2) Modifying  list  'b' is  as  good  as  modifying  list  'a'  becoz  'a'  and  'b'  point  to  same  list
'''



# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80] #Here we are defining the local list with 4 elements
	print(b) 				 #Prints the list b
# End  of  the  function
a = [10 , 20 , 30 , 40] 	 #Here GV points to a list
print(a) 					 #Prints the list a
change(a)                    #Here we are passing the list a to the function call prints the list b 
print(a)  					 #Prints the list a 



#  Find  outputs  (Home  work)
def   f1(x): 
	x = 20 
	print(x)
# End  of   the   function
x = 10 			#X is a GV with value 10
print(x) 		#Prints the value of x i.e 10
f1(x) 			#Function is called and prints the value of LV x where inside the function LV gets more priority so prints 20
print(x) 		#Prints the value of GV x i.e 10




#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25 
#end  of  the  function
a = (10 , 20 , 15 , 18)  #Gv a points the tuple of elements
print(a) 				 #Prints the tuple a i.e (10 , 20 , 15 , 18)
f1(a) 					 #Error #Tuple cannot be modified
print(a) 				 #Prints the tuple a i.e (10 , 20 , 15 , 18)




# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x #Here square points to the lambda function and default argument is used 
print(square(5))				   #Calling the lambda function passing positional argument 5 and returns 5**5 i.e 25
print(square()) 				   #Calling the lambda function without any arguments so default argument is passed i.e 100




# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))    # Here we are defining the lambda function and also calling the function i.e 7 7**7 = 49
print( lambda   x  :  x * x(7))       # Prints the type and address of the function i.e <function <lambda> at 0x00000260D5C8E3E0>
print( lambda   x  :   x * x) 	      # Here we are calling the lambda function without any arguments so it prints the type and address
print( (lambda  x = 25 :  x * x) () ) # Here we are calling the function without any arguments so default argument is passed and prints the result i.e 625
square = lambda  x :  x  *  x      	  # Here we are defining the lambda function 
print(square(5))  				      # Here we are calling the function with argument 5 i.e 25




add = lambda a,b : a + b      # Defines a lambda function to return sum of two arguments
print(type(add))              # Prints <class 'function'>
print(add(10 , 20))           # Prints 30
print(add(10.6 , 20.8))       # Prints 31.4
print(add('Hyder' , 'abad'))  # Prints 'Hyderabad'
print(add(True , False))      # Prints 1
print(add(25 , 10.8))         # Prints 35.8
print(add(3 + 4j , 5 + 6j))   # Prints (8+10j)
print(add(10 , '20'))         # Error: int + str is not supported
print(add())                  # Error: missing 2 required arguments
print(add)                    # Prints the lambda function object with its memory address


#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) 	#Here 10 and 20 positional arguments are passed to lambda function i.e 10 + 20 i.e 30
print(add()) 			#Prints the sum of default arguments i.e 3


#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) 							    # Here 10 and 20 positional arguments are passed to lambda function i.e 10 + 20 i.e 30
print(add()) 										# Prints the sum of default arguments i.e 3
print((lambda  x , y : x + y) ('Hyder' , 'abad'))   # Here two strings are concatinated i.e 'Hyderabad'
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))  # Here type and address is printed 




#  Find  outputs (Home  work)
large = lambda a ,b : max(a,b) 		#Here i have used max() to determine the largest element among both a and b
print(large(10  ,  20)) 	   		#Prints the 20
print(large(10.7  ,  5.6)) 	    	#Prints the 10.7
print(large('g'  ,  's'))  	   		#Prints the 's'
print(large('Rama'  ,  'Rajesh')) 	#Prints the 'Rama'
print(large(True  ,  False)) 		#Prints the True




#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b # Here we have defined the lambda function and passed the default arguments a and b and returns the a**b
print(power(2 , 3)) 					   # Returns the output as 2**3 i.e 8
print(power(4.5 , 4)) 					   # Returns the output as 4.5**4 i.e 410.06
print(power())  						   # Returns the output using default arguments i.e 3.5 ** 2 i.e 12.2
print(power(9))  						   # Returns the output as 9 ** 2 i.e 81




# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b) # Here we are defining the lambda function with a, b arguments and returning a tuple
x = all(10 , 7) 										# Here x points to the lambda function call
print(type(x)) 											# Prints the type i.e <class 'tuple'>
print(x) 												# Prints the result of 10 + 7 , 10-7, 10*7, 10/7 i.e (17, 3, 70, 1.4)
p , q , r , s = all(9 , 2) 								# Here we are calling the functon and unpacking the tuple elements i.e p = 11,q = 7,r = 18, s = 4.5
print(p) #11
print(q) #7
print(r) #18
print(s) #4.5




#  Find  outputs
a  =  lambda  :  'Hyd' #Here lambda function returns the String i.e 'Hyd'
print(a()) 			   #Prints the String 'Hyd'
print(a)               #Prints the type and address




# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb') #Here we are defining the lambda function and only 1st print statement is taken and rest of them are taken as next line before function call
print(a()) 													  #Prints the 'Hyd'
#output will be Sec
#               Cyb
#               Hyd 
#               none as function is not returning anthing so it returns none



# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')   # Here lambda function is defined and then prints the Sec 
#                                                                                                          Cyb
print(a()) 												# Prints the output as i.e 'Hyd'


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb') #Here a points to a tuple prints Sec
																							#  Cyb
print(type(a))  											  # Prints the type i.e <class 'tuple'>
print(a) 													  # Prints the type and address ,	None, None
for  x  in  a:
	print(x) 												  # Prints the elements of tuple i.e type and address
                                            #  None
											#  None
#a() #Error #we are calling the tuple not lambda function
print(a[0]()) #Type and address
			  #Hyd
			  #None



#  Find  outputs  (Home  work)
s = 'Hyd' 										# S points to the string Hyd
print(lambda  s  :  print(s)) 					# Prints the only type and address as we are defining and printing the lambda function
print(lambda  x  :  print(x) (s)) 				# Prints the type and address 
print((lambda  x  :  print(x)) (s)) 			# Here function is defined and called so prints the Hyd and returns None
(lambda  x  :  print(x)) (s) 					# Here function is defined and called Hyd




# Find outputs  (Home  work)
x = 5 								#Here x points to value 5 and it is a global variable
adder1 = lambda  y , x = x  : x + y #Lambda function is defined 
x = 10 								# Here x is modified to value 10
adder2 = lambda  y , x = x : x + y 	#Lambda function is defined
x = 20 								#X value is modified to 20
print(adder1(100)) 					#105
print(adder2(200)) 					#220
print(adder1(300 , 400)) #300 + 400 i.e 700




# Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4] #Here the list of lambda functions 
for   fun   in   a: #Here we are iterating the list 
        print(fun(5))
        
'''output:
25
125
625
'''
		


#  Find  outputs
def   f1(): #Here function is defined 
	print('Hyd') 
def   f2(): 
	print('Sec')
a = [f1 , f2] #Here ref a points to list of functions
for  x  in  a:
	     x() #Hyd #Sec
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')] #Error
print(a) #Type and address




# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4} #Ref a points to dict key-value pairs
key = 'power_3' #Here key points to key power_3
print(a[key]) #Prints the type and address
print(a[key](5)) #Prints the 125



# Find  outputs  (Home  work)
def   f1(x): #Here function is defined
        return  lambda  n  :  x ** n #lambda function is returned to the function call
lamb = f1(3)  #Here ref lamb points to function call
print(type(f1)) #<class 'function'>
print(type(lamb)) #<class 'function'> #It is a lambda function
print(lamb(2)) #3 ** 2 i.e 9
print(lamb(5)) #5 ** 5 i.e 243
print(lamb) # prints the type and address
print(lamb())  #Error #Here lambda function expects one argument but we are not passing 0 arguments 



# Find  outputs   (Home  work)
def   eval(a , b , c): #Here we are defining the regular function with 3 formal parameters
        return   lambda    x  :    a *   x **  2  +   b * x  +  c #Here we are returing the lambda function
lam  = eval(3 , 4 , 5) #Here ref lam points to the function call 
print(lam(2)) # Here we are calling the lambda function with argument x = 2 return the result : 25
print(lam(2.5)) # Here we are calling the lambda function with argument x = 2.5 return the result : 33.75
print(lam(4))# Here we are calling the lambda function with argument x = 4 return the result : 69




#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y #Here add points to the lambda function and that lambda functions returns the another lambda function  
a = add #Here a points to lambda function where add points to 
print(a(20)) #30
print(add(30)(40)) #70



# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0)) #Ref a points to nested tuple
b = sorted(a) #Here a is sorted by 1st element of the inner tuples 
print(b) #Prints the sorted nested list i.e inside list tuples i.e [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print() #Prints nothing
c = sorted(a , reverse = True) #Here nested tuple is sorted in bigger to smaller and returns the list
print(c) #Here list of tuples are printed i.e [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print() #Prints nothing
d = sorted(a ,  key =  lambda   x  :  x[1]) #Here We are using lambda function to sort the inner tuples based on the second element
print(d) #Returns the list of tuples which are sorted based on the second element i.e [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print() #Prints nothing
e = sorted(a , key =  lambda   x  :  x[2]) #Based on third element of inner tuples
print(e) #Prints the list of tuples i.e [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print() #Prints nothing
f = sorted(a , key = lambda   x  :  x[0]) #Based on 1st element of inner tuples
print(f) #prints the sorted list of inner tuples i.e [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print() #Prints nothing
g = sorted(a , key = lambda  x : x[1] , reverse = True) #Here sorted based on second element and in bigger to smaller order
print(g) #Prints the sorted tuple [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
#print(sorted(a , key = x[1])) #Error #Here x is not defined



a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
      {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
      {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ] #Here ref a points to list of dict
b = sorted(a , key=lambda x : x['Year']) #Here we are sorting based on the 'Year' key of each dict 
print(b) #Prints the sorted list of dicts i.e [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
#print(sorted(a)) #Error #Because Python does not know how to compare 2 dict objects directly





# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) #prints the max tuple based on 0th index element of inner tuple i.e (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] )) ##prints the max tuple based on 1st index element of inner tuple i.e (15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) #prints the max tuple based on 2nd index element of inner tuple i.e (20, 'Sita', 2800.0)
print(max(a)) #Prints the max tuple and based on 0th index by default i.e (25, 'Kiran', 1500.0)


# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) #False
add = lambda  x = 25 :   x == 35
print(add()) #False
#add = lambda  x  :   x = 25 #Error 
#add = lambda  x  :   x := 25 #Error



'''
There  are  21  matchsticks.
User  can  pick  1 , 2 , 3  or  4  matchsticks.
Computer  picks  after  user  and  whoever  picks  the  last  matchstick, they  lose  the  game.
Write  a  program  such  that  computer  wins

Logic:  Total  should  be  5

Hint: Use while  loop

						n = 21
   Iteration     user         computer             n
-------------------------------------------------------------
         1          2          3               n = 21 - 5 = 16

		 2          3          2               n = 16 - 5 = 11

		 3          1          4               n = 11 - 5 = 6

		 4          4          1               n =6 - 5 = 1
---------------------------------------------------------------
'''

'''
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  3
Computer  picks  2 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  0
Input  can  not  be >  4  nor  <  1,  Reenter  :  1
Computer  picks  4 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  2
Computer  picks  3 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  5
Input  can  not  be >  4  nor  <  1,  Reenter  :  6
Input  can  not  be >  4  nor  <  1,  Reenter  :  7
Input  can  not  be >  4  nor  <  1,  Reenter  :  8
Input  can  not  be >  4  nor  <  1,  Reenter  :  4
Computer  picks  1 matchsticks
You  have  lost  the  game  and  Computer  wins
''' 
n = 21
while n != 1:
	user = int(input("How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :"))
	while user > 4 or user < 1:
		user = int(input("Input can not be > 4 nor < 1, Reenter : "))
	computer = user - 5
	print(f'computer picks {5-user} matchsticks')
	n -= 5
print("You have lost the game and Computer wins")